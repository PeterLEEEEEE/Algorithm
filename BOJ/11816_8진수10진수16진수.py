num = input()

if num[:2] == '0x':
    print(int(num, 16))
elif num[0] == '0':
    print(int(num, 8))
else:
    print(int(num))
