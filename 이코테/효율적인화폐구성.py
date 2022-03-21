N, M = map(int, input().split())
coin = []

dp = [10001] * (M+1)
dp[0] = 0
dp[2] = 1
dp[3] = 1

for _ in range(N):
    coin.append(int(input()))

for i in range(N):
    for j in range(4, M+1):
        dp[j] = min(dp[j], dp[j-coin[i]] + 1)

if dp[M] == 10001:
    print(-1)
else:
    print(dp[M])
