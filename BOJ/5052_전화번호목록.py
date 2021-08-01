import sys

t = int(input())

for _ in range(t):
    n = int(input())
    arr = []

    for _ in range(n):
        arr.append(sys.stdin.readline().rstrip())
    
    arr.sort()
    
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1][:len(arr[i])]:
            print('NO')
            break
    else:
        print('YES')