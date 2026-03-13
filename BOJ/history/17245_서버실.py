import sys

input = sys.stdin.readline
N = int(input())

com_batch = []
computers = 0
max_com = 0 
cnt = 0
for _ in range(N):
    row = list(map(int, input().split()))
    com_batch.append(row)
    computers += sum(row)
    max_com = max(max_com, max(row))

start, end = 0, max_com
lev = 0

while start <= end:
    mid = (start + end) // 2
    cur_sum = 0
    for i in range(N):
        for j in range(N):
            if mid > com_batch[i][j]:
                cur_sum += com_batch[i][j]
            else:
                cur_sum += mid
    
    if cur_sum >= computers / 2:
        lev = mid
        end = mid - 1
    else:
        start = mid + 1

print(lev)