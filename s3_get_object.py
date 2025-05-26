import boto3
import botocore.exceptions
import sys
import logging
logger = logging.getLogger(__name__)
logging.basicConfig(filename='example.tmp', encoding='utf-8', level=logging.DEBUG)


def get_object(bucket, object_key):
    try:
        obj = s3.Object(bucket, object_key)
        body = obj.get()['Body'].read()
        logger.info("Got object '%s' from bucket '%s'.", object_key, bucket)
    except botocore.exceptions.ClientError:
        logger.exception(("Couldn't get object '%s' from bucket '%s'.", object_key, bucket))
        raise
    else:
        return body

s3 = boto3.resource('s3')

X = get_object("testfmorenodpublichtml", "BoardingPass2.pdf")
print(X)

## Commands to review

# aws s3 cp tiny10_23h1_x64.iso s3://franciscomoreno/

# aws s3api head-object --bucket franciscomoreno  --key Photos_5thGrade.zip

# aws s3api head-object --bucket franciscomoreno  --key ControlStructure.png

# aws s3 presign s3://franciscomoreno/Photos_5thGrade.zip --expires-in 1500

#Using curl -o DownloadedPhotos.zip 'XXX'

# See https://github.com/realokun/aws/blob/master/s3/get_product.py for complex use of S3 Object lambda

# Select from a defined file called productCatalog, to find s3 select you have to choose file and choose actions

# Query: select s.Title from s3object[*].Products[*] s where s.id=209