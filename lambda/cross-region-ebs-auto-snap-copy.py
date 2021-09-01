import sys

try:
    import boto3

    print("imported boto3 successfully")
except Exception as e:
    print(e)
    sys.exit(1)
source_region = 'eu-west-1'
destination_region = 'eu-west-2'
session = boto3.session.Session(profile_name='cooper')
ec2_source_client = session.client(service_name='ec2', region_name=source_region)
sts_client = session.client(service_name='sts', region_name=source_region)
account_id = sts_client.get_caller_identity().get('Account')
print(account_id)
all_snaps = []
f_bkp = {"Name": "tag:env", "Values": ["dev"]}
for each_snap in ec2_source_client.describe_snapshots(OwnerIds=[account_id], Filters=[f_bkp]).get('Snapshots'):
    all_snaps.append(each_snap.get('SnapshotId'))
    print(all_snaps)

ec2_des_client = session.client(service_name='ec2', region_name=destination_region)
for each_source_snap in all_snaps:
    print("taking backup for id of {} into of {}".format(each_source_snap, destination_region))
    ec2_des_client.copy_snapshot(
        Description="Disaster recovery",
        SourceRegion=source_region,
        DestinationRegion=destination_region,
        SourceSnapshotId=each_source_snap,
    )
print("EBS Snapshot copy destination region completed")
print("Modifying tags")
for each_source_snap in f_bkp:
    ec2_source_client.delete_tags(
        Resources=[each_source_snap],
        Tags=[
            {
                'Key': 'env',
                'Value': 'dev'
            }
        ]
    )
    print("Creating new tags for {}".format(each_source_snap))
    ec2_source_client.create_tags(
        Resources=[each_source_snap],
        Tags=[
            {
                'Key': 'env',
                'Value': 'dev-copy'
            }
        ]
    )
