import pandas as pd
class DataValidator:
    @staticmethod
    def validate(data, expected_data):
        # Placeholder for validation logic
        return data.equals(expected_data)
    @staticmethod
    def validate_extracted_data(extracted_file_path, expected_file_path):
        """Validate that the extracted data matches expected values."""
        extracted_data = pd.read_csv(extracted_file_path)
        expected_data = pd.read_csv(expected_file_path)

        if extracted_data.equals(expected_data):
            print("Validation succeeded: Extracted data matches expected data.")
            return True
        else:
            print("Validation failed: Extracted data does NOT match expected data.")
            print("Differences:")
            print(extracted_data.compare(expected_data))
            return False
