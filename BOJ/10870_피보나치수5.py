N = int(input())

dp = [0, 1]
temp = 0

for i in range(2, N+1):
    temp = dp[i-1] + dp[i-2]
    dp.append(temp)
print(dp[N])