# tests/test_e2e.py
from concurrent.futures import ThreadPoolExecutor

import pytest
from src.mongodb_handler import read_profile_attributes
from src.file_extractor import extract_data_from_flat_file, save_extracted_data
from src.data_validator import validate_extracted_data
from src.s3_handler import upload_to_s3

@pytest.mark.parametrize("profile_name, input_file, expected_file, output_file, s3_key", [
    ("MemberDataProfile", './data/input/members1.txt', './data/expected/members1.csv', './data/output/extracted_data1.csv','output/extracted_data1.csv'),
    ("MemberDataProfile", './data/input/members2.txt', './data/expected/members2.csv', './data/output/extracted_data2.csv','output/extracted_data2.csv'),
    # Add more cases as needed
])
def test_e2e_workflow(profile_name, input_file, expected_file, output_file, s3_key):
    attributes = read_profile_attributes(profile_name)
    assert attributes is not None, "Profile attributes should not be None"

    intermediary_data = extract_data_from_flat_file(input_file, attributes)
    assert len(intermediary_data) > 0, "Extracted data should not be empty"

    save_extracted_data(intermediary_data, output_file)

    assert validate_extracted_data(output_file, expected_file), "Data validation should pass"

    # Parallel upload to S3
    with ThreadPoolExecutor() as executor:
        future = executor.submit(upload_to_s3, output_file, s3_key)
        future.result()  # Wait for the upload to complete