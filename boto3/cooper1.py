import boto3

aws_man_con = boto3.Session(profile_name="default")
iam_con = aws_man_con.resource("iam")

for iam_user in iam_con.users.all():
    print(iam_user.name)

iam_con_client = aws_man_con.client(service_name="iam")
for iam_client in iam_con_client.all():
    print(iam_client.name)