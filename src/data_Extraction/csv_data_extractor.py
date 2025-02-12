import pandas as pd
class CsvDataExtractor:
    def extract(self, file_path,attribute):
        # Read the CSV file
        data = pd.read_csv(file_path)
        return data