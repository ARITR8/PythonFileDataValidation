# src/file_extractor.py

import pandas as pd


def extract_data_from_flat_file(file_path, attributes):
    intermediary_data = []

    with open(file_path, 'r') as f:
        for line in f:
            record = {}
            for attr in attributes:
                start_pos = attr['start_position']
                length = attr['length']
                value = line[start_pos:start_pos + length].strip()  # Strip to remove extra spaces
                record[attr['attribute_name']] = value

            intermediary_data.append(record)

    return intermediary_data


def save_extracted_data(intermediary_data, output_file_path):
    """Write intermediary extracted data to a CSV file."""
    df = pd.DataFrame(intermediary_data)
    df.to_csv(output_file_path, index=False)
    print(f"Extracted data saved to {output_file_path}.")