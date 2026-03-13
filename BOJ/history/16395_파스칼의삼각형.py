import sys

input = sys.stdin.readline

n, k = map(int, input().split())

dp = [[1]*i for i in range(1, 32)]

dp[0] = [1]
dp[1] = [1, 1]
dp[2] = [1, 2, 1]

for i in range(3, n+1):
    for j in range(1, len(dp[i])-1):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

print(dp[n-1][k-1])