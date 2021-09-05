import bcrypt

pw = 'dududungman123!!'
salt = bcrypt.gensalt()

password = bcrypt.hashpw(pw.encode(), salt)


print(password.decode())
