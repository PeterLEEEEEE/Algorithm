import re
while True:
    password = input()

    if not re.match("^(?=.*\d)[\d]{9,11}$", password):
        print('not match')
    else:
        print('match')
