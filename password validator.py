import re

email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
password_regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~])[A-Za-z\d!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]{8,}$"


def email_checker(email):

    if re.fullmatch(email_regex, email):
        print('Valid Email')
    else:
        print('Invalid Email')


def password_checker(password):

    if re.match(password_regex, password):
        print('Valid Password')
    else:
        print('Invalid Password')


my_email = input('Type your email: ')
my_password = input('Type your password: ')

email_checker(my_email)
password_checker(my_password)
