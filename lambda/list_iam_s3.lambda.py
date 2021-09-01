import boto3


def lambda_handler(event, context):
    # TODO implement
    # session = boto3.session.Session(profile='cooper')
    # iam_con_re = session.resource(service_name='iam', region_name='eu-west-1')
    print("your users in your account are:")
    iam_con_re = boto3.resource(service_name='iam')
    for each_iam in iam_con_re.users.all():
        print(each_iam.name)
    s3_con_re = boto3.resource('s3', 'eu-west-1')
    for each_s3 in s3_con_re.buckets.all():
        print("Your buckets in eu-west-1 are:")
        print(each_s3.name)
