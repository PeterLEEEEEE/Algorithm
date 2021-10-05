n, k = map(int, input().split())

coins = []
for _ in range(n):
    coins.append(int(input()))

coins.sort()

dp = [10001] * (k + 1)
dp[0] = 0

for i in range(1, k+1):
    for coin in coins:
        if i - coin < 0:
            break
        dp[i] = min(dp[i], dp[i-coin] + p1)

if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])
