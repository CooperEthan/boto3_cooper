import boto3
import sys

aws_man_con = boto3.session.Session(profile_name='cooper')
ec2_con_re = aws_man_con.resource(service_name='ec2', region_name='eu-west-1')
ec2_con_cli = aws_man_con.client(service_name='ec2', region_name='eu-west-1')

while True:
    print("this script perform fallowing actions on ec2 instance")
    print(""""
    1. start
    2. stop
    3. terminate
    4. Exit
    """)
    opt = int(input("Enter your option: "))
    if opt == 1:
        instance_id = input("Enter your EC@ Instance Id: ")
        my_req_instance = ec2_con_re.Instance(instance_id)
        # print(dir(my_req_instance))
        print("Starting ec2 instance ....")
        my_req_instance.start()
    elif opt == 2:
        instance_id = input("Enter your EC@ Instance Id: ")
        my_req_instance = ec2_con_re.Instance(instance_id)
        print("Stopping ec2 instance ....")
        my_req_instance.stop()
    elif opt == 3:
        instance_id = input("Enter your EC@ Instance Id: ")
        my_req_instance = ec2_con_re.Instance(instance_id)
        print("Terminating ec2 instance ....")
        my_req_instance.terminate()
    elif opt == 4:
        instance_id = input("Enter your EC@ Instance Id: ")
        print("Exiting ec2 instance ....")
    else:
        print("your action is invalid")
