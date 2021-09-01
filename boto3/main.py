import boto3

aws_mng_con = boto3.Session(profile_name="default")
iam_con = aws_mng_con.resource("iam")

for each_user in iam_con.users.all():
    print(each_user.name)

s3_con = aws_mng_con.resource("s3")

for each_bucket in s3_con.buckets.all():
    print("\n" + "bucket names are ")
    print(each_bucket.name)

# listing iam user with client object
#iam_cli = aws_mng_con.client(service_name="iam",region_name="eu-west-1")

#for each_user in iam_cli.all():
 #   print(iam_cli.name)


