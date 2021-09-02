import bcrypt

pw = 'dissgo12'
salt = bcrypt.gensalt()

password = bcrypt.hashpw(pw.encode(), salt)




print(password.decode())
