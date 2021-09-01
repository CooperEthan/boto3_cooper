import boto3
import boto3_type_annotations

aws_man_con = boto3.session.Session(profile_name="default")
iam_con_re = aws_man_con.resource(service_name='iam', region_name='eu-west-1')
ec2_con_re = aws_man_con.resource(service_name='ec2', region_name='eu-west-1')
# s3_con_re = aws_man_con.resource(service_name='s3', region_name='eu-west-1')

# for iam in iam_con_re.users.all():
#    print(iam.name)

# for s3 in s3_con_re.buckets.all():


def delete_bucket():
    # s3_con_re = aws_man_con.resource(service_name='s3', region_name='eu-west-1')
    # response = s3_con_re.bucket.delete(ExpectedBucketOwner='599326816772')
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('cooper-boto3')
    bucket.objects.all().delete()


delete_bucket()
