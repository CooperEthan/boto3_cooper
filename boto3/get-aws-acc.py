import boto3

aws_acc_man = boto3.session.Session(profile_name='cooper')
client = aws_acc_man.client(service_name='sts')
response = client.get_caller_identity()

print(response)