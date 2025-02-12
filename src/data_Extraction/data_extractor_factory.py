from botocore.compat import file_type

from .csv_data_extractor import CsvDataExtractor
from .json_data_extractor import JsonDataExtractor
from .text_data_extractor import TextDataExtractor
class DataExtractorFactory:
    @staticmethod
    def create_extractor(file_type):
        if file_type == 'csv':
            return CsvDataExtractor()
        elif file_type == 'json':
            return JsonDataExtractor()
        elif file_type=='txt':
            return TextDataExtractor()
        raise ValueError(f"Unknown file type: {file_type}")
