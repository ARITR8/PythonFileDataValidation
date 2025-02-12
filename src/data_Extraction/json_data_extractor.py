import pandas as pd
class JsonDataExtractor:
    def extract(self, file_path,attribute):
        # Read the JSON file
        data = pd.read_json(file_path)
        return data