n = input()

for i in n:
    if i.islower():
        print(i.upper(), end='')
    else:
        print(i.lower(), end='')
