import boto3

aws_man_con = boto3.session.Session(profile_name='cooper')
ec2_con_re = aws_man_con.resource(service_name='ec2', region_name='eu-west-1')
ec2_con_cli = aws_man_con.client(service_name='sts', region_name='eu-west-1')
# client = aws_man_con.client(service_name='sts')
response = ec2_con_cli.get_caller_identity()
acc_id = response.get('Account')
print(acc_id)

for each in ec2_con_re.snapshots.filter(OwnerIds=[acc_id]):
    print(each)
