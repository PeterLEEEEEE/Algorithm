# 너무 어렵다 진짜 ㅋㅋㅋㅋㅋㅋㅋㅋ 

n = int(input())
time = []
pay = []

for _ in range(n):
    t, p = map(int, input().split())
    time.append(t)
    pay.append(p)

dp = [0] * (n + max(time))

for i in range(n):
    if dp[i] > dp[i+1]: 
        dp[i+1] = dp[i]

    if dp[i + time[i]] < dp[i] + pay[i]:
        dp[i + time[i]] = dp[i] + pay[i]

print(dp)



