import boto3

#We are going to use S3 bucket service
s3=boto3.resource('s3')


#print all bucket names
for bucket in s3.buckets.all():
    print(bucket)
s3.create_bucket()
# "D:\AWS\AWS_tutorial\AWS_Boto3_Course\S3 Bucket\HousePricePrediction.csv"
# upload file to s3 bucuket
# with open("D:\AWS\AWS_tutorial\AWS_Boto3_Course\S3 Bucket\HousePricePrediction.csv",'rb') as data:
#     s3.Bucket('grir').put_object(Key="D:\AWS\AWS_tutorial\AWS_Boto3_Course\S3 Bucket\HousePricePrediction.csv",Body=data)
print(s3)