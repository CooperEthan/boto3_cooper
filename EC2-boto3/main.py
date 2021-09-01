import boto3

aws_man_con = boto3.session.Session(profile_name='cooper')

ec2_cli = aws_man_con.client(service_name='ec2')

response = ec2_cli.describe_instances()['Reservations']
# print(response['Reservations'])

for each_item in response:
    for each in each_item['Instances']:
        print("=========================")
        print(" The Image Id is: {}\n The Instance Id is: {}".format(each['ImageId'], each['InstanceId']))

print("=====================")
responseV = ec2_cli.describe_volumes()['Volumes']
print(responseV)
for each_volumes in responseV:
    print(" The Volume Id is: {}\n The Volume Type Is: {}".format(each_volumes['VolumeId'], each_volumes['VolumeType']))
