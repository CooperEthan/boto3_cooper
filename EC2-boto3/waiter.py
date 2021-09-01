import time

import boto3

aws_con = boto3.session.Session(profile_name='cooper')
ec2_con_re = aws_con.resource(service_name='ec2', region_name='eu-west-1')
ec2_con_cli = aws_con.client(service_name='ec2', region_name='eu-west-1')

'''
# Waiter with Resource
# my_ins = ec2_con_re.Instance('i-0c0b9c9fff2fe882e')
# print("starting ec2 instance")
# print(my_ins.state['Name'])
# my_ins.start()
# my_ins.wait_until_running() 
'''
'''
# Waiter with client
print("starting ec2 instances")
ec2_con_cli.start_instances(InstanceIds=['i-0c0b9c9fff2fe882e'])

waiter = ec2_con_cli.get_waiter('instance_running')

waiter.wait(InstanceIds=['i-0c0b9c9fff2fe882e'])

print("instance is up and running")
'''
# print(dir(my_ins))


'''
while True:
    my_ins = ec2_con_re.Instance('i-0c0b9c9fff2fe882e')
    print("your current status of instance is: " + my_ins.state['Name'])
    if my_ins.state['Name'] == "running":
        break
    print("Waiting to get running status")
    time.sleep(5)
print("instance is up and running")
'''
# my_ins.stop()
