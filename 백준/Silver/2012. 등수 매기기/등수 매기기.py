import sys

input = sys.stdin.readline

N = int(input())

arr = []
for _ in range(N):
  arr.append(int(input()))

arr.sort()
ans = 0

for i in range(1, N+1):
  ans += abs(i - arr[i-1])


print(ans)
