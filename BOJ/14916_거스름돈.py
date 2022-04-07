import sys

input = sys.stdin.readline

n = int(input())

dp = [0 for _ in range(n+6)]
dp[2] = 1
dp[3] = 0
dp[4] = 2
dp[5] = 1

for i in range(6, n+1):
    if i % 5 == 0:
        dp[i] = dp[i-5] + 1
    else:
        dp[i] = dp[i-2] + 1

if dp[n] == 0:
    print(-1)
else:
    print(dp[n])

print(dp)
