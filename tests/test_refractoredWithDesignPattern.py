import glob
import pytest
from src.data_Extraction.data_extractor_factory import DataExtractorFactory
from src.data_validation.data_validator import DataValidator
from src.data_storage.mongo_operations import insert_status_record, delete_all_records , read_profile_attributes
from src.data_storage.s3_handler import upload_to_s3
from config.config import S3_BUCKETS, PROFILE_COLLECTION, PROFILE_NAME
from src.data_saver.text_data_saver import TextDataSaver
import uuid
import time


@pytest.fixture(scope="module", autouse=True)
def cleanup_before_tests():
    """Fixture to clean up MongoDB collection before tests."""
    delete_all_records()  # Clear existing records
    yield
    delete_all_records()  # Optional: clean up after tests


@pytest.fixture(scope="module")
def input_files():
    input_directory = './data/input/*.txt'
    return glob.glob(input_directory)


@pytest.mark.parametrize("bucket_index", range(len(S3_BUCKETS)))  # Parameterize with bucket indices
def test_e2e_workflow(input_files, bucket_index):
    unique_id = str(uuid.uuid4())  # Generate a unique ID for current session

    for input_file in input_files:
        file_type = input_file.split('.')[-1]  # Determine the file type
        extractor = DataExtractorFactory.create_extractor(file_type)  # Factory pattern usage
        attributes = read_profile_attributes(PROFILE_NAME)
        assert attributes is not None, "Profile attributes should not be None"
        data = extractor.extract(input_file,attributes)  # Extract data using the appropriate extractor
        assert len(data) > 0, "Extracted data should not be empty"
        expected_file = input_file.replace('input', 'expected').replace('.txt', '.csv')
        output_file = input_file.replace('input', 'output').replace('.txt', '_extracted.csv')
        print("********************" + output_file)
        saver = TextDataSaver()
        saver.save(data, output_file)

        # expected_file = input_file.replace('input', 'expected').replace('.txt', '.csv')
        # output_file = input_file.replace('input', 'output').replace('.txt', '_extracted.csv')
        s3_key = f'output/{output_file.split("/")[-1]}'

        # Validate the extracted data (add your actual validation logic)
        #expected_data = ...  # Load the expected data accordingly
        assert DataValidator.validate_extracted_data(output_file, expected_file), "Data validation should pass"

        # Insert statuses into MongoDB
        for status in ["Pending", "In Progress", "Completed"]:
            insert_status_record(unique_id, input_file, status)
            time.sleep(3)  # Simulate processing time

        # Upload data to S3 Bucket
        upload_to_s3(output_file, bucket_index , s3_key)  # Upload to the specified S3 bucket