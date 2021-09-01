import boto3

# aws_man_con = boto3.session.Session(profile_name='cooper')
# ec2_con_re = aws_man_con.resource(service_name='ec2', region_name='eu-west-1')
ec2_con_re = boto3.resource(service_name='ec2', region_name='eu-west-1')

for each_instance in ec2_con_re.instances.all():
    print(each_instance.id, each_instance.state)

print(dir(ec2_con_re.instances))