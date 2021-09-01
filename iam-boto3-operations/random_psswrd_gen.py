from random import choice
import boto3

len_of_password = 8
valid_chars_for_passwords = "eknge;noi44053802"
password = []
'''
for each in range(len_of_password):
    password.append(choice(valid_chars_for_passwords))
random_pass = "".join(password)
print(random_pass)
'''

random_pass = "".join(choice(valid_chars_for_passwords) for each_char in range(len_of_password))
print(random_pass)
