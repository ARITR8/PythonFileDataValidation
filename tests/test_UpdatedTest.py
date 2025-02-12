import pytest
from src.mongodb_handler import read_profile_attributes
from src.file_extractor import extract_data_from_flat_file, save_extracted_data
from src.data_validator import validate_extracted_data
from src.s3_handler import upload_to_s3
from config import S3_BUCKETS

# Use a counter for round-robin bucket assignment
bucket_counter = 0
# List of S3 bucket names


@pytest.mark.parametrize("profile_name, input_file, expected_file, output_file, s3_key, bucket_name", [
    ("MemberDataProfile", './data/input/members1.txt', './data/expected/members1.csv', './data/output/extracted_data1.csv','output/extracted_data1.csv',S3_BUCKETS[0]),
    ("MemberDataProfile", './data/input/members2.txt', './data/expected/members2.csv', './data/output/extracted_data2.csv','output/extracted_data2.csv',S3_BUCKETS[1]),
    # ("MemberDataProfile", './data/input/members3.txt', './data/expected/expected_data3.csv', './data/output/extracted_data3.csv','output/extracted_data3.csv'),
    # ("MemberDataProfile", './data/input/members4.txt', './data/expected/expected_data4.csv', './data/output/extracted_data4.csv','output/extracted_data4.csv'),
    # ("MemberDataProfile", './data/input/members5.txt', './data/expected/expected_data5.csv', './data/output/extracted_data5.csv','output/extracted_data5.csv'),
    # ("MemberDataProfile", './data/input/members6.txt', './data/expected/expected_data6.csv', './data/output/extracted_data6.csv','output/extracted_data6.csv'),
    # # Add more cases as needed
])
@pytest.mark.parametrize("s3_bucket_idx", range(len(S3_BUCKETS)))  # Add parameterization for selecting S3 bucket index
def test_e2e_workflow(profile_name, input_file, expected_file, output_file, s3_key , s3_bucket_idx, bucket_name):
    global bucket_counter  # Use the global bucket counter
    attributes = read_profile_attributes(profile_name)
    assert attributes is not None, "Profile attributes should not be None"

    intermediary_data = extract_data_from_flat_file(input_file, attributes)
    assert len(intermediary_data) > 0, "Extracted data should not be empty"

    save_extracted_data(intermediary_data, output_file)

    assert validate_extracted_data(output_file, expected_file), "Data validation should pass"

    # Upload to the specified S3 bucket
    upload_to_s3(output_file, s3_key, bucket_name)  # Pass the bucket name directly

    # # Determine which bucket to use based on the test case index
    # bucket_to_use = S3_BUCKETS[s3_bucket_idx % len(S3_BUCKETS)]
    #
    # # Parallel upload to S3
    # with ThreadPoolExecutor() as executor:
    #     future = executor.submit(upload_to_s3, output_file, s3_key, s3_bucket_idx)
    #     future.result()  # Wait for the upload to complete