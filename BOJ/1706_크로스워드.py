import sys

input = sys.stdin.readline

R, C = map(int, input().split())
arr = []
checker = []
for i in range(R):
    arr.append(input().rstrip())

print(arr[1][1])

for i in range(R):
    temp = ''
    for j in arr[i]:
        if j == '#':
            if len(temp) >= 2:
                checker.append(temp)
            temp = ''
            
        else:
            temp += j
    if len(temp) >= 2:
        checker.append(temp)

print(checker)

for i in range(C):
    for j in arr[j][i]:
        temp = ''
    for j in arr[i]:
        if j == '#':
            if len(temp) >= 2:
                checker.append(temp)
            temp = ''
            
        else:
            temp += j
    if len(temp) >= 2:
        checker.append(temp)

print(checker)