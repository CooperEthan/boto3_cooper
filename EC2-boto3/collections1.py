import boto3

aws_man_con = boto3.session.Session(profile_name='cooper')
ec2_con_re = aws_man_con.resource(service_name='ec2', region_name='eu-west-1')
ec2_con_cli = aws_man_con.client(service_name='ec2', region_name='eu-west-1')
f1 = {"Name": "instance-state-name", "Values": ["running", "stopped"]}
f2 = {"Name": "instance-type", "Values": ["t2.micro"]}
dev_instances = []
f3 = {"Name": "tag:Name", "Values": ["dev"]}
for each in ec2_con_cli.describe_instances(Filters=[f3])['Reservations']:
    for each_item in each['Instances']:
        dev_instances.append(each_item['InstanceId'])
ec2_con_cli.start_instances(InstanceIds=dev_instances)

waiter = ec2_con_cli.get_waiter('instance_running')
# for each in ec2_con_re.instances.filter(Filters=[f1, f2]):
#    print(each)
# ec2_con_re.instances.start()
print("Starting Dev instances.....")
# waiter.wait(InstanceIds=['i-0c0b9c9fff2fe882e', 'i-05da381bcf979bd04'])
waiter.wait(InstanceIds=dev_instances)
print("your instance is up and running")





