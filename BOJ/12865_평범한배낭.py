n, weight = map(int, input().split())

dp = [[0]*(weight+1) for _ in range(n)]

for i in range(n):
    w, v = map(int, input().split())
    for j in range(w, weight+1):
        dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)

print(dp)