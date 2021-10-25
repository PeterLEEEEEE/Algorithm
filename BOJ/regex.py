import re
while True:
    email = input()

    if not re.match('^[a-zA-Z\d+-.]+@[a-zA-Z\d+-.]+\.[a-zA-Z]{2,3}$', email):
        print('not match')
    else:
        print('match')
