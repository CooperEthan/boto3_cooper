import boto3
from pprint import pprint

session = boto3.session.Session(profile_name='cooper')
list_of_volumeIds = []
ec2_con_cli = session.client(service_name='ec2', region_name='eu-west-1')
filter_dev = {"Name": "tag:environment", "Values": ["dev", "test"]}
for each_volume in ec2_con_cli.describe_volumes(Filters=[filter_dev])['Volumes']:
    # pprint(each_volume['VolumeId'])
    list_of_volumeIds.append(each_volume['VolumeId'])
    print(list_of_volumeIds)

# paginator collects it page by page
paginator = ec2_con_cli.get_paginator('describe_volumes')
for each_page in paginator.paginate(Filters=[filter_dev]):
    for each_vol in each_page['Volumes']:
        list_of_volumeIds.append(each_vol['VolumeId'])
# print(list_of_volumeIds)
SnapIds = []
for each_volume_id in list_of_volumeIds:
    print(each_volume_id)
    waiter = ec2_con_cli.get_waiter('snapshot_completed')
    response = ec2_con_cli.create_snapshot(
        Description='taking snap with lambda and cloudwatch',
        VolumeId=each_volume_id,
        TagSpecifications=[
            {
                'ResourceType': 'snapshot',
                'Tags': [
                    {
                        'Key': 'Delete-on',
                        'Value': '90'
                    },
                ]
            },
        ],
    )
    response.get('SnapshotId')
    SnapIds.append(response.get('SnapshotId'))
print(SnapIds)
#  print("Taking the snap Ids", response.get('SnapshotId'))
waiter.wait()
print('snapshots has been created successfully')
print("Completed snapshots of volumes of {}".format(list_of_volumeIds))
