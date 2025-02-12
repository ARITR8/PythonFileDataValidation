import pandas as pd
from src.data_saver.abstract_data_saver import DataSaver  # Adjust import according to your project structure

# class TextDataSaver(DataSaver):
#     def save(self,intermediary_data, output_file_path):
#         # """Write intermediary extracted data to a CSV file."""
#         # df = pd.DataFrame(intermediary_data)
#         # df.to_csv(output_file_path, index=False)
#         # print(f"Extracted data saved to {output_file_path}.")
#         """Write intermediary extracted data to a CSV file in chunks."""
#         # Create an empty DataFrame
#         """Write intermediary extracted data to a CSV file in chunks."""
#         chunk_size = 100000
#         # Initialize a counter for the number of records written
#         record_count = 0
#
#         with open(output_file_path, 'w', newline='', encoding='utf-8') as f:
#             # Write the header only once
#             f.write('ID,Name,Email,Phone\n')  # Adjust the header based on your data
#
#             # Process intermediary_data in chunks
#             for i in range(0, len(intermediary_data), chunk_size):
#                 # Get a chunk of records
#                 chunk = intermediary_data[i:i + chunk_size]
#
#                 # Convert the chunk to a DataFrame
#                 df = pd.DataFrame(chunk)
#
#                 # Append to CSV file (overwrite if the file is empty)
#                 df.to_csv(f, index=False, header=False)
#
#                 record_count += len(df)
#
#         print(f"Extracted data saved to {output_file_path} with {record_count} records.")

class TextDataSaver:
    def save(self, intermediary_data, output_file_path, data_type):
        chunk_size = 100000
        record_count = 0

        if data_type == 'member':
            header = 'member_id,member_name,member_address\n'
        elif data_type == 'bank':
            header = 'member_id,bank_account_number,bank_balance\n'

        with open(output_file_path, 'w', newline='', encoding='utf-8') as f:
            f.write(header)

            for i in range(0, len(intermediary_data), chunk_size):
                chunk = intermediary_data[i:i + chunk_size]
                df = pd.DataFrame(chunk)
                df.to_csv(f, index=False, header=False)
                record_count += len(df)

        print(f"Extracted {data_type} data saved to {output_file_path} with {record_count} records.")