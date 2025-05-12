import boto3

# Return type: dict / additional API calls needed to get objects
def listClient():
    s3client = boto3.client('s3')
    response = s3client.list_objects_v2(Bucket='testfmorenodpublichtml')
    for content in response['Contents']:
        print(content['Key'], content['LastModified'])
        #print(content)
        print(dir(content))

# Resources represent an object-oriented interface to AWS. They provide a
# higher-level abstraction than the raw, low-level calls made by service clients
def listResource():
    s3resource = boto3.resource('s3')
    bucket = s3resource.Bucket('testfmorenodpublichtml')
    for object in bucket.objects.all():
        print(object.key, object.last_modified)
        #print(object.meta)
        #print(object)
        print(dir(object))
        

listClient()
print("-----")
listResource()