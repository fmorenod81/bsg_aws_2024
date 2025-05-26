import boto3

# Create S3 resource using custom session
session = boto3.session.Session(profile_name='staging')

# Retrieve region from session object
current_region = "us-west-2"


# Create a high-level resource from custom session
resource = session.resource('s3')
bucket = resource.Bucket('notes-bucket-21052025')


# Region-specific endpoints require the LocationConstraint parameter
X=bucket.create(
    CreateBucketConfiguration={
        'LocationConstraint': current_region
    }
)

print("Done")