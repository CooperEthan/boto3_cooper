import boto3
from botocore.exceptions import ClientError

cnt = 1
session = boto3.session.Session(profile_name='cooper')
s3_re = session.resource(service_name='s3', region_name='eu-west-1')
bucket_name = 'cooper-boto3'
# resource object
'''bucket_object = s3_re.Bucket(bucket_name)
for each_obj in bucket_object.objects.all():
    print(each_obj.key)
    cnt=cnt+1'''

# client object
s3_cli = session.client(service_name='s3', region_name='eu-west-1')
bucket_object = s3_cli.list_objects(
    Bucket=bucket_name)['Contents']
for each_objects in bucket_object:
    print(cnt, each_objects['Key'])
    cnt = cnt + 1


'''def delete_bucket():
    s3_buck = s3_re.Bucket(bucket_name)
    s3_buck.objects.all().delete()


delete_bucket()
print("successfully deleted the objects")'''


def encrypt_bucket():
    response = s3_cli.list_buckets()
    for bucket in response['Buckets']:
        try:
            enc = s3_cli.get_bucket_encryption(Bucket=bucket[bucket_name])
            rules = enc['ServerSideEncryptionConfiguration']['Rules']
            print('Bucket: %s, Encryption: %s' % (bucket[bucket_name], rules))
        except ClientError as e:
            if e.response['Error']['Code'] == 'ServerSideEncryptionConfigurationNotFoundError':
                print('Bucket: %s, no server-side encryption' % (bucket[bucket_name]))
            else:
                print("Bucket: %s, unexpected error: %s" % (bucket[bucket_name], e))


encrypt_bucket()
# paginator object
'''s3_cli = session.client(service_name='s3', region_name='eu-west-1')
paginator = s3_cli.get_paginator('list_objects')
for each_page in paginator.paginate(Bucket=bucket_name):
    for each_pa in each_page['Contents']:
        print(cnt, each_pa['Key'])
        cnt = cnt + 1'''
