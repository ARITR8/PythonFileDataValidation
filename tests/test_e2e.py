# tests/test_e2e.py

import unittest
from src.mongodb_handler import read_profile_attributes
from src.file_extractor import extract_data_from_flat_file, save_extracted_data
from src.data_validator import validate_extracted_data
#from src.s3_handler import upload_to_s3

class TestEndToEndProcess(unittest.TestCase):

    def setUp(self):
        self.test_cases = [
            {
                "profile_name": "MemberDataProfile",
                "input_file": './data/input/members1.txt',
                "expected_file": './data/expected/expected_data1.csv',
                "output_file": './data/output/extracted_data1.csv',
                "s3_key": "output/extracted_data1.csv"
            },

        ]

    def run_single_test_case(self, case):
        attributes = read_profile_attributes(case['profile_name'])
        self.assertIsNotNone(attributes, "Profile attributes should not be None")

        intermediary_data = extract_data_from_flat_file(case['input_file'], attributes)
        self.assertGreater(len(intermediary_data), 0, "Extracted data should not be empty")

        save_extracted_data(intermediary_data, case['output_file'])

        validation_result = validate_extracted_data(case['output_file'], case['expected_file'])
        self.assertTrue(validation_result, "Data validation should pass")

      #  upload_to_s3(case['output_file'], case['s3_key'])

    def test_all_cases(self):
        for case in self.test_cases:
            with self.subTest(case=case):
                self.run_single_test_case(case)

if __name__ == "__main__":
    unittest.main()