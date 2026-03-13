n = int(input())

arr = list(map(int, input().split()))


dp = [1] * n
rdp = [1] * n
ans = 0
rarr = arr[::-1]

for i in range(1, n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)
        if rarr[j] < rarr[i]:
            rdp[i] = max(rdp[i], rdp[j] + 1)

rdp = rdp[::-1]

for i in range(n):
    if dp[i] + rdp[i] > ans:
        ans = dp[i] + rdp[i]

print(ans - 1)
