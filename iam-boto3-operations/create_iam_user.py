import sys
from random import choice

import boto3


def get_iam_client_object():
    session = boto3.session.Session(profile_name='cooper')
    iam_client = session.client(service_name='iam', region_name='eu-west-1')
    return iam_client


def get_random_password():
    len_of_password = 8
    valid_chars_for_password = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    return "".join(choice(valid_chars_for_password) for each_char in range(len_of_password))


def main():
    iam_client = get_iam_client_object()
    Iam_user_name = "Co"
    password = get_random_password()
    PolicyArn = "arn:aws:iam::aws:policy/AdministratorAccess"
    # iam_client.delete_user(UserName='CE')

    try:
        iam_client.create_user(UserName=Iam_user_name)
    except Exception as e:
        print("Iam User already exists")
        sys.exit()
    iam_client.create_login_profile(UserName=Iam_user_name, Password=password, PasswordResetRequired=False)
    iam_client.attach_user_policy(UserName=Iam_user_name, PolicyArn="arn:aws:iam::aws:policy/AdministratorAccess")
    print("Iam User Name = {} and Password = {}".format(Iam_user_name, password))


if __name__ == '__main__':
    main()

# to delete user, first iam_client.delete_login_profile(Username=''), then delete policies,
# then delete iam_client.delete_user(Username='')

