mul = 1
for _ in range(3):
    num = int(input())
    mul *= num

mul = str(mul)
nums = '0123456789'
arr = []

for i in mul:
    arr.append(i)

for i in nums:
    if i in mul:
        print(mul.count(i))
    else:
        print(0)
