import sys

input = sys.stdin.readline

N, K = map(int, input().split())

arr = list(input().rstrip())
ans = 0

# PHPPHHHPP
for i in range(N):
  if arr[i] == 'P':
    for j in range(max(i-K, 0), min(i+K+1, N)):
      if arr[j] == 'H':
        arr[j] = 'X'
        ans += 1
        break

print(ans)