import boto3
from config.config import S3_BUCKETS

s3_client = boto3.client('s3')
def upload_to_s3(file_path, bucket_index, s3_key):
    S3_BUCKET_NAME = S3_BUCKETS[bucket_index]
    s3_client.upload_file(file_path, S3_BUCKET_NAME, s3_key)