import boto3

s3=boto3.client('s3')

resource=s3.list_buckets()

print(resource['Buckets'])

#Creating a bucket
