import glob
import pytest
import uuid
import time
from src.data_Extraction.data_extractor_factory import TextDataExtractor
from src.data_storage.mongo_operations import MongoOperations
from src.data_saver.text_data_saver import TextDataSaver
from config.config import S3_BUCKETS, PROFILE_NAME

mongo_operations = MongoOperations()


@pytest.fixture(scope="module", autouse=True)
def cleanup_before_tests():
    """Fixture to clean up MongoDB collection before tests."""
    mongo_operations.delete_all_records()  # Clear existing records
    yield
    mongo_operations.delete_all_records()  # Optional: clean up after tests


@pytest.fixture(scope="module")
def input_files():
    input_directory = './data/input/*.txt'
    return glob.glob(input_directory)


@pytest.mark.parametrize("bucket_index", range(len(S3_BUCKETS)))  # Parameterize with bucket indices
def test_e2e_workflow(input_files, bucket_index):
    unique_id = str(uuid.uuid4())

    for input_file in input_files:
        file_type = input_file.split('.')[-1]  # Determine the file type
        attributes = mongo_operations.read_profile_attributes(PROFILE_NAME)  # Fetch attributes
        assert attributes is not None, "Profile attributes should not be None"

        # extractor = DataExtractorFactory.create_extractor(file_type)  # Factory pattern usage
        # Extract member info
        # member_extractor = TextDataExtractor(attributes)
        # member_data = member

# Extract member info
        member_extractor = TextDataExtractor(attributes)
        member_data = member_extractor.extract(input_file)
        assert len(member_data) > 0, "Extracted member data should not be empty"

        # Save member data
        member_output_path = input_file.replace('input', 'output').replace('.txt', '_members.csv')
        member_saver = TextDataSaver()
        member_saver.save(member_data, member_output_path, data_type='member')

        # Extract bank info - similar implementation can be applied for bank records
        bank_extractor = TextDataExtractor(attributes)  # Ensure the attributes for bank data are fetched
        bank_data = bank_extractor.extract(input_file)
        assert len(bank_data) > 0, "Extracted bank data should not be empty"

        # Save bank data
        bank_output_path = input_file.replace('input', 'output').replace('.txt', '_banks.csv')
        bank_saver = TextDataSaver()
        bank_saver.save(bank_data, bank_output_path, data_type='bank')

        ###############below coce need to edit.

