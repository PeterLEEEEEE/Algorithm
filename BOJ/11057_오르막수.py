n = int(input())

dp = [[1] * 10 for _ in range(n)]

for i in range(1, n):
    sum_val = 0
    for j in range(10):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
        

print(dp)

