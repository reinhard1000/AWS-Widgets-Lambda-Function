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
            return{
                "statusCode":200,
                "headers":{},
                "body":json.dumps(body)
            }
        
        return{
            "statusCode": 400,
            "headers": {},
            "body": "We only accept GET /"
        }
    except Exception as e:
        body = e.__srt__() or json.dumps(e, indent=2)
        return {
            "statusCode": 400,
            "headers": {},
            "body": json.dumps(body)
        }
