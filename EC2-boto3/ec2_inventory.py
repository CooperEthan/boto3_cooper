import boto3

aws_man_con = boto3.session.Session(profile_name='cooper')
ec2_con_cli = aws_man_con.client(service_name='ec2', region_name='eu-west-1')
ec2_con_re = aws_man_con.resource(service_name='ec2', region_name='eu-west-1')
cnt = 1
for each in ec2_con_re.instances.all():
    print(cnt, each.id, each.instance_type, each.launch_time.strftime("%Y-%m-%d"), each.private_ip_address)
    cnt += 1
