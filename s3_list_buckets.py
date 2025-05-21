import boto3

# Low-Level call
s3_client = boto3.client('s3')


# Retrieve the list of existing buckets
response = s3_client.list_buckets()# Output the bucket names
print('Existing buckets:')
for bucket in response['Buckets']:
    print(f' {bucket["Name"]}')
