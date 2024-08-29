# List object int bucket using the Resource API
# Return type : ObjectSummary
# Resource represents an object oriented interface to Amazon Web Services (AWS)
# They provide a higher-level abstraction than the raw, low-level calls made by service clients.

import boto3

def listResource():
    s3resource = boto3.resource('s3')
    bucket = s3resource.Bucket('DOC-EXAMPLE-BUCKET')
    for obj in bucket.objects.all():
        print(obj.key,obj.last_modified)
    return

listResource()

