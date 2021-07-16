'''
C언어식으로 풀었으나 
num = int(input(), 16) 이렇게 한줄로도 가능하다...

'''
num = input()
loop = len(num)
nums = ['0', '1', '2', '3', '4', '5', '6', '7',
        '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

dec = 0
num = num[::-1]
if loop == 1:
    print(nums.index(num))
else:
    for i in range(loop):
        dec += ((16**i) * nums.index(num[i]))

    print(dec)
