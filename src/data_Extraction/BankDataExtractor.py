from src.data_Extraction.text_data_extractor import TextDataExtractor


class BankDataExtractor(TextDataExtractor):
    def __init__(self, attributes):
        super().__init__(attributes)