import boto3

# Low-level call
s3_client = boto3.client('s3')


# Retrieve the list of existing buckets
paginator = s3_client.get_paginator('list_objects')
page_iterator = paginator.paginate(Bucket='franciscomoreno', PaginationConfig={'MaxItems': 3})
for page in page_iterator:
    print("---")
    print(len(page['Contents']))
    print(page['Contents'])
    print("---")

