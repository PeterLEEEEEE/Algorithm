n = input()

arr = list(n)
key = '0'
mul = 0
checker = 0

if key not in arr:
    checker = -1
else:
    arr.remove('0')
    arr.append('0')

for i in arr:
    mul += int(i)

if mul % 3 != 0:
    checker = -1
else:
    arr.sort(reverse=True)

if checker == -1:
    print(-1)
else:
    print(''.join(arr))
