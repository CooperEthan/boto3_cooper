import boto3

iam_con = boto3.resource("s3")

for s3 in iam_con.buckets.all():
    print(s3)

iam_con = boto3.resource("iam")

for iam in iam_con.users.all():
    print(iam.name)