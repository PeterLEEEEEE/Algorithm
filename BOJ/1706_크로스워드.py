import sys

input = sys.stdin.readline

R, C = map(int, input().split())
arr = []
checker = []
for i in range(R):
    arr.append(input().rstrip())


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



for i in range(C):
    temp = ''
    for j in range(R):
        
        if arr[j][i] == '#':
            if len(temp) >= 2:
                checker.append(temp)
            temp = ''
            
        else:
            temp += arr[j][i] 
    
    if len(temp) >= 2:
        checker.append(temp)

checker.sort() 
print(checker[0])