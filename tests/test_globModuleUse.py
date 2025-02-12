import os
import glob
import time
import uuid

import pytest

from src.mongoOperationsStatus import insert_status_record,delete_all_records
from src.mongodb_handler import read_profile_attributes
from src.file_extractor import extract_data_from_flat_file, save_extracted_data
from src.data_validator import validate_extracted_data
from src.s3_handler import upload_to_s3
from config import S3_BUCKETS
#from src.mongo_operationsA import insert_status_record, delete_all_records

@pytest.fixture(scope="module", autouse=True)
def cleanup_before_tests():
    """Fixture to clean up the MongoDB collection before running tests."""
    delete_all_records()  # Delete all records from the collection
    yield  # This allows the test to run after cleanup
    delete_all_records()  # Optionally clear records again after tests

# Fixture to gather input files dynamically
@pytest.fixture(scope="module")
def input_files():
    # Assuming your input files are in the data/input directory
    input_directory = './data/input/*.txt'  # Change the pattern to match your actual files
    return glob.glob(input_directory)


@pytest.mark.parametrize("bucket_name", S3_BUCKETS)  # Parameterize buckets
def test_e2e_workflow(input_files, bucket_name):
    # Generate a unique ID for the session
    unique_id = str(uuid.uuid4())
    for input_file in input_files:
        profile_name = "MemberDataProfile"
        expected_file = input_file.replace('input', 'expected').replace('.txt', '.csv')
        output_file = input_file.replace('input', 'output').replace('.txt', '_extracted.csv')
        print("********************"+output_file)
        s3_key = f'output/{output_file}'  # Set the S3 key based on output file name

        attributes = read_profile_attributes(profile_name)
        assert attributes is not None, "Profile attributes should not be None"

        intermediary_data = extract_data_from_flat_file(input_file, attributes)
        assert len(intermediary_data) > 0, "Extracted data should not be empty"

        save_extracted_data(intermediary_data, output_file)

        assert validate_extracted_data(output_file, expected_file), "Data validation should pass"

        # Upload to the specified S3 bucket
        upload_to_s3(output_file,s3_key, bucket_name )

        # Update status in MongoDB
        for status in ["Pending", "In Progress", "Completed"]:
            insert_status_record(unique_id, os.path.basename(input_file), status)
            time.sleep(3)  # Simulate delay for status update (3 seconds)

        # Upload to the specified S3 bucket
        upload_to_s3(output_file, bucket_name, s3_key)