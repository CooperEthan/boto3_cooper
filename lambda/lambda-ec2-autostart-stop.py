import boto3


def lambda_handler(event, context):
    # TODO implement
    ec2_con_re = boto3.resource('ec2', 'eu-west-1')
    filter_dev = {"Name": "tag:environment", "Values": ["dev"]}
    for each_ec2 in ec2_con_re.instances.filter(Filters=[filter_dev]):
        print(each_ec2.id)
        each_ec2.stop()
        print("starting dev instances")
