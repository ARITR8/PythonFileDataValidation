# src/main.py

from config.config import DB_NAME
from src.mongodb_handler import read_profile_attributes
from src.file_extractor import extract_data_from_flat_file, save_extracted_data

def main():
    # Step 1: Define the profile name
    profile_name = "MemberDataProfile"  # Adjust as necessary

    # Step 2: Read profile attributes from MongoDB
    attributes = read_profile_attributes(profile_name)

    if attributes is None:
        print(f"No profile found with name: {profile_name}")
        return

    # Step 3: Define the path to the input flat file
    file_path = './data/input/members.txt'  # Adjust as necessary

    # # Step 4: Extract data from flat file based on attributes
    # intermediary_data = extract_data_from_flat_file(file_path, attributes)
    #
    # # Step 5: Save the extracted data to CSV
    # output_file_path = './data/output/extracted_data.csv'  # Adjust as necessary
    # save_extracted_data(intermediary_data, output_file_path)

if __name__ == "__main__":
    main()