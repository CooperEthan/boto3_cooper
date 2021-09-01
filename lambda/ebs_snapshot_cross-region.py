import boto3
import botocore

session = boto3.session.Session(profile_name='cooper')
ec2_con_cli = session.client(service_name='ec2', region_name='eu-west-1')
all_regions = []
for each_region in ec2_con_cli.describe_regions()['Regions']:
    all_regions.append(each_region.get('RegionName'))

for each_region in all_regions:
    print('Working on  {}'.format(each_region))
    ec2_con_cli = session.client(service_name='ec2', region_name=each_region)

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
    if bool(list_of_volumeIds) == False:
        continue
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
        try:
            response.get('SnapshotId')
        except botocore.exceptions.ClientError as e:
            continue
        SnapIds.append(response.get('SnapshotId'))
    print(SnapIds)
    print("Taking the snap Ids", response.get('SnapshotId'))
    waiter.wait()
    print('snapshots has been created successfully')
    print("Completed snapshots of volumes of {}".format(list_of_volumeIds))
