import sys

input = sys.stdin.readline

n = int(input())

dp = [0] * (10001)
dp[1] = 1
dp[2] = 1

if 0 <= n <= 2:
    print(dp[n])
else:
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    print(dp[n])