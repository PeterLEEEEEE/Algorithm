import sys

input = sys.stdin.readline

N = int(input())

dp = [0 for _ in range(81)]

dp[1] = 4
dp[2] = 6
dp[3] = 10
dp[4] = 16

if N >= 5:
    for i in range(5, N+1):
        dp[i] = dp[i-1] + dp[i-2]

print(dp[N])