import sys
import botocore
import boto3

try:
    import boto3
except ModuleNotFoundError:
    print("Boto3 is not installed")
except Exception as e:
    print(e)
    sys.exit()

try:
    aws_man_con=boto3.session.Session(profile_name='dev')
except botocore.exceptions.ProfileNotFound:
    print("dev profile not configured")

try:
    aws_man_con = boto3.session.Session(profile_name='s3')
    iam_con_re = aws_man_con.resource(service_name='iam')
    for each_user in iam_con_re.users.all():
        print(each_user)
except botocore.exceptions.ClientError:
    print("This is a client error")
except Exception as e:
    print(e)