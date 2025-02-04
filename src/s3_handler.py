# src/s3_handler.py

import boto3
from config.config import S3_BUCKET_NAME

s3_client = boto3.client('s3')

def upload_to_s3(file_path, s3_key):
    """Upload a file to an S3 bucket."""
    try:
        s3_client.upload_file(file_path, S3_BUCKET_NAME, s3_key)
        print(f"File {file_path} uploaded to S3 as {s3_key}.")
    except Exception as e:
        print(f"Error uploading file to S3: {e}")