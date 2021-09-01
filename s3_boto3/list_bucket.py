import boto3

session = boto3.session.Session(profile_name='cooper')
s3_re = session.resource('s3', 'eu-west-1')
print("Using Resource Object:")
for each_bucket in s3_re.buckets.all():
    print(each_bucket.name)

s3_cli = session.client('s3', 'eu-west-1')
print("Using Client Object:")
for list_buckets in s3_cli.list_buckets()['Buckets']:
    print(list_buckets.get('Name'))
