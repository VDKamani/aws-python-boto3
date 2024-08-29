# make a service client request to describe the instances in the account
import boto3
ec2 = boto3.client('ec2')
response = ec2.describe_instances()
print(response)
