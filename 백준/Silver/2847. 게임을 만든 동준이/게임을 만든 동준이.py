import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
  arr.append(int(input()))

ans = 0
arr = arr[::-1]

for i in range(N-1):
  start = arr[i]
  if start > arr[i+1]:
    continue
  else:
    temp = arr[i+1] - (start-1)
    arr[i+1] = arr[i+1] - temp
    ans += temp

print(ans)