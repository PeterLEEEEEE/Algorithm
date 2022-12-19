import re
pattern = "([^A-Za-z0-9가-힣-_])"

print(''.join(re.findall(pattern, 'asdasd_1-검A !')))
