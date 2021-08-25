n = int(input())

dp = [[1] * 10 for _ in range(n+1)]

for i in range(1, n+1):
    sum_val = 0
    for j in range(10):
        dp[i][j] = sum(dp[i-1][:j+1])
        sum_val = dp[i][j]

print(sum_val % 10007)

