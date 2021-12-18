from collections import deque

n, k = map(int, input().split())

def bfs():
    q = deque()
    q.append(n)
    while q:
        temp = q.popleft()
        if temp == k:
            print(arr[temp])
            break
        for i in (temp-1, temp+1, temp*2):
            if 0 <= i <= arr_len and not arr[i]:
                arr[i] = arr[temp] + 1
                q.append(i)

arr_len = 10 ** 5
arr = [0] * (arr_len+1)
bfs()

