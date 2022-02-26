from collections import deque

t = int(input())

ans = deque()

for _ in range(t):
    n = int(input())
    arr = input().split()
    flag = arr[0]
    ans.append(flag)

    for i in range(1, len(arr)):
        if arr[i] <= flag:
            flag = arr[i]
            ans.appendleft(arr[i])
        else:
            ans.append(arr[i])
    
    print(''.join(ans))
    ans.clear()


