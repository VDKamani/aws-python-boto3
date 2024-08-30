import boto3

BUCKET_NAME = 'BUCKET_NAME'
FILE_NAME = 'index.html'

# setup s3 client named s3_client
s3_client = boto3.client('s3')
# create a function to put s3 bucket ownership controls with Rules set to BucketOwnerPreferd    
def put_s3_bucket_ownership_controls():
    response = s3_client.put_bucket_ownership_controls(
        Bucket=BUCKET_NAME,
        OwnershipControls={
            'Rules': [
                {
                    'ObjectOwnership': 'BucketOwnerPreferred'
                }
            ]
        }
    )
    return response
# create a function to set public access block values to false 
def set_public_access_block():
    response = s3_client.put_public_access_block(
        PublicAccessBlockConfiguration={
            'BlockPublicAcls': False,
            'IgnorePublicAcls': False,
            'BlockPublicPolicy': False,
            'RestrictPublicBuckets': False
        },
        Bucket=BUCKET_NAME
    )
    return response
# create a function to allow public access to FILE_NAME
def allow_public_access():
    response = s3_client.put_object_acl(
        ACL='public-read',
        Bucket=BUCKET_NAME,
        Key=FILE_NAME
    )
    return response
# call the functions
put_s3_bucket_ownership_controls()
set_public_access_block()
allow_public_access()



