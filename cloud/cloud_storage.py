import boto3
import os

aws_access_key = 'YOUR_AWS_ACCESS_KEY'
aws_secret_key = 'YOUR_AWS_SECRET_KEY'
region_name = 'YOUR_AWS_REGION'
s3_bucket_name = 'your-s3-bucket-name'
s3_client = boto3.client('s3',
                         aws_access_key_id=aws_access_key,
                         aws_secret_access_key=aws_secret_key,
                         region_name=region_name)

def upload_file(file_path, s3_key):
    try:
        s3_client.upload_file(file_path, s3_bucket_name, s3_key)
        print(f"File {file_path} uploaded to S3 with key {s3_key}.")
    except Exception as e:
        print(f"Error uploading file to S3: {str(e)}")

def download_file(s3_key, file_path):
    try:
        s3_client.download_file(s3_bucket_name, s3_key, file_path)
        print(f"File {s3_key} downloaded from S3 to {file_path}.")
    except Exception as e:
        print(f"Error downloading file from S3: {str(e)}")

def list_files(prefix=''):
    try:
        response = s3_client.list_objects_v2(Bucket=s3_bucket_name, Prefix=prefix)
        if 'Contents' in response:
            for obj in response['Contents']:
                print(f"File: {obj['Key']}, Size: {obj['Size']}")
        else:
            print("No files found.")
    except Exception as e:
        print(f"Error listing files in S3: {str(e)}")

def main():
    local_file_path = 'path/to/your/local/file.txt'
    s3_key = 'folder/in/s3/file.txt'
    upload_file(local_file_path, s3_key)
    download_file(s3_key, 'path/to/downloaded/file.txt')
    list_files('folder/in/s3/')

if __name__ == "__main__":
    main()
