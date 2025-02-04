# Data Processing Project

## Overview
This project is designed to read data from flat files, process the data, validate the output, and upload results to an Amazon S3 bucket. The project demonstrates end-to-end data processing capabilities, integration with AWS, and thorough testing with unit and end-to-end tests.

## Folder Structure
    ```

    /data-processing
    │
    ├── /config            # Configuration settings (e.g., MongoDB URI, S3 Bucket name)
    │   ├── config.py
    │   └── constants.py
    │
    ├── /data
    │   ├── /input        # Input flat files (e.g., members1.txt, members2.txt)
    │   ├── /output       # Processed output files (e.g., extracted_data1.csv)
    │   ├── /expected     # Expected output files for validation (e.g., expected_data1.csv)
    │   └── /temp         # Optional: Temporary files during processing
    │
    ├── /src
    │   ├── init.py    # Package initialization
    │   ├── mongodb_handler.py  # Functions to interact with MongoDB
    │   ├── file_extractor.py   # Functions to extract data from flat files
    │   ├── data_validator.py    # Functions to validate extracted data
    │   ├── s3_handler.py        # Functions to handle S3 uploading
    │
    ├── /tests
    │   ├── test_e2e.py      # End-to-end tests for the complete workflow
    │   ├── test_mongodb_handler.py # Unit tests for MongoDB operations
    │   ├── test_file_extractor.py   # Unit tests for data extraction logic
    │   └── test_data_validator.py    # Unit tests for validation logic
    │
    └── README.md             # Project overview, setup instructions, and usage details


## Prerequisites
- Python 3.x
- Libraries used:
    - `pymongo`
    - `boto3`
    - `pandas`
    - `pytest`
    - Optional: `html-testRunner` for HTML reporting

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd data-processing

   Set Up a Virtual Environment:
Create and activate a virtual environment:

    ```bash

       python -m venv .venv
     .venv\Scripts\activate  # On Windows


# source .venv/bin/activate  # On macOS/Linux
Install Required Libraries:
Create a requirements.txt file, or install required libraries manually:
        ```bash
        
        pip install pymongo boto3 pandas pytest 

Configure AWS and MongoDB Settings:
Edit config/config.py and set your MongoDB URI and S3 Bucket name:

       ```
          MONGO_URI = "your_mongodb_uri"
    DB_NAME = "your_database"
    S3_BUCKET_NAME = "your_bucket_name"

Usage
Run Tests
To run the end-to-end tests:

        ```bash
        pytest tests/test_e2e.py




Notes
Ensure that you have valid AWS credentials configured either via environment variables or the AWS credentials file (~/.aws/credentials).
Adjust the input and expected files to your data needs within the /data folder.
Contributing
Feel free to fork the repository and submit pull requests. Contributions are welcome!

License
This project is licensed under the MIT License. See the LICENSE file for details.


### Summary

This structure ensures that everything is formatted correctly in Markdown, making it easy to read and maintain. Each section conveys essential information about your project, including setup instructions, folder structure, and usage guidelines. If there are any specific adjustments you’d like to make or additional sections you want to include, feel free to let me know!
