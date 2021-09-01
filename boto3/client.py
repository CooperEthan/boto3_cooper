import boto3
import boto3_type_annotations

aws_man_con = boto3.session.Session(profile_name="default")

# iam,ec2 and s3

iam_con_cli = aws_man_con.client(service_name="iam", region_name="eu-west-1")
ec2_con_cli = aws_man_con.client(service_name="ec2", region_name="eu-west-1")
s3_con_cli = aws_man_con.client(service_name="s3", region_name="eu-west-1")

# list all iam user using client object

iam = (iam_con_cli.list_users())
print(iam["Users"])

ec2 = ec2_con_cli.describe_instances()

#print(ec2['Reservations'])

for each_item in ec2['Reservations']:
    for each_instance in each_item['Instances']:
        print(each_instance)
        print(each_instance['InstanceId'])
