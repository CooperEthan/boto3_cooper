import boto3

session = boto3.session.Session(profile_name='cooper')
cnt = 1
'''iam_con_re = session.resource(service_name='iam', region_name='eu-west-1')
for each_user in iam_con_re.users.all():
    print(cnt, each_user.name)
    cnt = cnt + 1'''
iam_con_cli = session.client(service_name='iam')
paginator = iam_con_cli.get_paginator('list_users')
for each_us in paginator.paginate():
    for each_user_page in each_us['Users']:
        print(cnt, each_user_page['UserName'])
        cnt=cnt+1

iam_cli = session.client(service_name='ec2')
paginator = iam_cli.get_paginator('describe_instances')
for each_instance in paginator.paginate():
    ec2 = each_instance['Reservations']
    print(ec2)

