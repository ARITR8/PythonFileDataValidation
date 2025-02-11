import boto3
from config.config import S3_BUCKETS  # Import the S3 bucket names

s3_client = boto3.client('s3')

def upload_to_s3(file_path, s3_key, bucket_name):
    """Upload a file to an S3 bucket using the given bucket index."""
    # Choose the bucket name from the configuration based on the index
    S3_BUCKET_NAME = bucket_name # Get the appropriate bucket name

    try:
        s3_client.upload_file(file_path, S3_BUCKET_NAME, s3_key)
        print(f"File {file_path} uploaded to S3 bucket '{S3_BUCKET_NAME}' as '{s3_key}'.")
    except Exception as e:
        print(f"Error uploading file to S3 bucket '{S3_BUCKET_NAME}': {e}")