import boto3 as bt

s3=bt.client('s3')

resources=s3.list_buckets()
print(resources['Buckets'])


# for bucket in resources['Buckets']:
#     print(bucket)

# s3.create_bucket(Bucket="bucket_using_python")

#Delete objects (Files) fro bucket
# s3.delete_object(Bucket='grir', Key="D:\AWS\AWS_tutorial\AWS_Boto3_Course\S3 Bucket\HousePricePrediction.csv")

#get Object
# s3.get_object(Bucket='grir',Key="D:\AWS\AWS_tutorial\AWS_Boto3_Course\S3 Bucket\HousePricePrediction.csv")

# Deleting The bucket
# s3.delete_bucket(Bucket="grir")
# print(resources['Buckets'])

# print(resources.keys())
# print(s3)