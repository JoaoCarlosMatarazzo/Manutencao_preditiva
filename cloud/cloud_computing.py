import boto3
import json

# Configurações AWS para integrar e executar tarefas de 
# processamento em uma plataforma de computação em nuvem
aws_access_key = 'YOUR_AWS_ACCESS_KEY'
aws_secret_key = 'YOUR_AWS_SECRET_KEY'
region_name = 'YOUR_AWS_REGION'
lambda_function_name = 'YOUR_LAMBDA_FUNCTION_NAME'
s3_bucket_name = 'YOUR_S3_BUCKET_NAME'

lambda_client = boto3.client('lambda',
                             aws_access_key_id=aws_access_key,
                             aws_secret_access_key=aws_secret_key,
                             region_name=region_name)

s3_client = boto3.client('s3',
                         aws_access_key_id=aws_access_key,
                         aws_secret_access_key=aws_secret_key,
                         region_name=region_name)

def invoke_lambda(payload):
    response = lambda_client.invoke(
        FunctionName=lambda_function_name,
        InvocationType='RequestResponse',
        Payload=json.dumps(payload)
    )
    response_payload = json.loads(response['Payload'].read().decode('utf-8'))
    return response_payload

def upload_to_s3(data, key):
    s3_client.put_object(Bucket=s3_bucket_name, Key=key, Body=json.dumps(data))
    print(f"Uploaded data to S3 with key: {key}")

def main():
    payload = {
        "temperature": 25.3,
        "vibration": 0.8,
        "humidity": 55.0
    }
    result = invoke_lambda(payload)
    print(f"Result from Lambda: {result}")
    s3_key = 'results/lambda_output.json'
    upload_to_s3(result, s3_key)

if __name__ == "__main__":
    main()
