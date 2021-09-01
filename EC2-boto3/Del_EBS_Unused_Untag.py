import boto3

aws_man_con = boto3.session.Session(profile_name='cooper')
'''ec2_con_re = aws_man_con.resource(service_name='ec2', region_name='eu-west-1')
f_ebs_unused = {"Name": "status", "Values": ["available"]}
for each in ec2_con_re.volumes.filter(Filters=[f_ebs_unused]):
    if not each.tags:
        print(each.id, each.state, each.tags)
        print("Deleting unused and untagged volumes")
        each.delete()'''
ec2_con_cli = aws_man_con.client(service_name='ec2', region_name='eu-west-1')

for each in ec2_con_cli.describe_volumes()['Volumes']:
    if not 'Tags' in each and each['State'] == 'available':
        print("Deleting", each['VolumeId'])
        ec2_con_cli.delete_volume(VolumeId=each['VolumeId'])
