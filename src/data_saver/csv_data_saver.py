import pandas as pd
from abstract_data_saver import DataSaver  # Adjust import according to your project structure

class CSVDataSaver(DataSaver):
    def save(self, data, output_path):
        df = pd.DataFrame(data)
        df.to_csv(output_path, index=False)
        print(f"Extracted data saved to {output_path}.")