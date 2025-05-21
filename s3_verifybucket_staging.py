import boto3
import botocore.exceptions
import sys

def verifyBucketName(s3Client, bucket):
    try:
        ## check if a bucket already exists in AWS
        s3Client.head_bucket(Bucket=bucket)
        # If the previous command is successful, the bucket is already in your account.
        raise SystemExit('This bucket has already been created')
    except botocore.exceptions.ClientError as e:
        error_code = int(e.response['Error']['Code'])
        if error_code == 404:
            ## If you receive a 404 error code, a bucket with that name
            # does not exist anywhere in AWS.
            print('Existing Bucket Not Found, please proceed')
        if error_code == 403:
            ## If you receive a 403 error code, a bucket with that name exists 
            #  in another AWS account.
            raise SystemExit('This bucket is already owned by another AWS Account')
        else:
            # Something else has gone wrong.
            raise SystemExit('Undefined Error')

s3_client = boto3.client('s3')

verifyBucketName(s3_client, 'franciscomoreno')
