import json
import boto3
import zipfile
import os

# Configurações AWS
aws_access_key = 'YOUR_AWS_ACCESS_KEY'
aws_secret_key = 'YOUR_AWS_SECRET_KEY'
region_name = 'YOUR_AWS_REGION'
s3_bucket_name = 'your-s3-bucket-name'
lambda_function_name = 'your-lambda-function-name'

# Cliente Boto3 para S3 e Lambda
s3_client = boto3.client('s3',
                         aws_access_key_id=aws_access_key,
                         aws_secret_access_key=aws_secret_key,
                         region_name=region_name)

lambda_client = boto3.client('lambda',
                             aws_access_key_id=aws_access_key,
                             aws_secret_access_key=aws_secret_key,
                             region_name=region_name)

iam_client = boto3.client('iam',
                          aws_access_key_id=aws_access_key,
                          aws_secret_access_key=aws_secret_key,
                          region_name=region_name)

def create_s3_bucket(bucket_name):
    try:
        s3_client.create_bucket(Bucket=bucket_name,
                                CreateBucketConfiguration={'LocationConstraint': region_name})
        print(f"Bucket {bucket_name} created successfully.")
    except Exception as e:
        print(f"Error creating bucket: {str(e)}")

def create_lambda_role(role_name):
    assume_role_policy_document = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {
                    "Service": "lambda.amazonaws.com"
                },
                "Action": "sts:AssumeRole"
            }
        ]
    }
    try:
        role = iam_client.create_role(
            RoleName=role_name,
            AssumeRolePolicyDocument=json.dumps(assume_role_policy_document),
            Description='Role for Lambda function'
        )
        print(f"Role {role_name} created successfully.")
        return role['Role']['Arn']
    except Exception as e:
        print(f"Error creating role: {str(e)}")
        return None

def attach_policy_to_role(role_name, policy_arn):
    try:
        iam_client.attach_role_policy(
            RoleName=role_name,
            PolicyArn=policy_arn
        )
        print(f"Policy {policy_arn} attached to role {role_name}.")
    except Exception as e:
        print(f"Error attaching policy: {str(e)}")

def create_lambda_function(function_name, role_arn, zip_file_path):
    with open(zip_file_path, 'rb') as f:
        zipped_code = f.read()

    try:
        response = lambda_client.create_function(
            FunctionName=function_name,
            Runtime='python3.8',
            Role=role_arn,
            Handler='lambda_function.lambda_handler',
            Code=dict(ZipFile=zipped_code),
            Timeout=300,
            MemorySize=128
        )
        print(f"Lambda function {function_name} created successfully.")
    except Exception as e:
        print(f"Error creating Lambda function: {str(e)}")

def main():
    create_s3_bucket(s3_bucket_name)
    lambda_role_name = 'lambda_basic_execution'
    lambda_role_arn = create_lambda_role(lambda_role_name)
    attach_policy_to_role(lambda_role_name, 'arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole')

    if lambda_role_arn:
        zip_file_path = '/path/to/your/lambda_function.zip'
        with zipfile.ZipFile(zip_file_path, 'w') as z:
            z.write('lambda_function.py')
        create_lambda_function(lambda_function_name, lambda_role_arn, zip_file_path)

if __name__ == "__main__":
    main()
