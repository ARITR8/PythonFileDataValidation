
import pandas as pd

class TextDataExtractor:
    def __init__(self, attributes):
        self.attributes = attributes

    def extract(self, file_path):
        intermediary_data = []
        with open(file_path, 'r') as f:
            for line in f:
                record = {}
                for attr in self.attributes:
                    start_pos = attr['startPosition']
                    length = attr['length']
                    value = line[start_pos:start_pos + length].strip()
                    record[attr['fieldName']] = value
                intermediary_data.append(record)
        return intermediary_data