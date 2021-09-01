import boto3

def lambda_handler(event, context):
    # TODO implement
    ec2_con = boto3.resource('ec2','eu-west-1')
    sns_client = boto3.client('sns','eu-west-1')
    myec2_ins = ec2_con.Instance('i-073f8a2b1b3b9833a')
    print(myec2_ins.state['Name'])
    sns_client.publish(TargetArn='arn:aws:sns:eu-west-1:599326816772:codecommit-notifications-test',Message=myec2_ins.state['Name'])
