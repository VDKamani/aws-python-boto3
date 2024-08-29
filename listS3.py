# List Objects in buvket using the Client Api 
# Return type : Dict / additional API calls needed to get objects

def listClient():
    s3client = boto3.client('s3')
    response = s3client.list_objects_v2(Buket='DOC-EXAMPLE-BUCKET')
    for content in response['Contents']:
        print(content['key'],content['LastModified'])
    return