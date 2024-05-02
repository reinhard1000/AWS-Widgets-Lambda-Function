import boto3
import os
import json

s3 = boto3.client('s3');
bucketName = os.environ.get('BUCKET');

def main(event, context):
    try:
        method = event['httpMethod']

        if(method == "GET"):
            if event['path'] == '/':
                data =s3.list_objects_v2(Bucket=bucketName)
                body = {
                    "widgets": [obj['Key'] for obj in data['Contents']]
                }
    except Exception as e:
        body = {
            
        }
