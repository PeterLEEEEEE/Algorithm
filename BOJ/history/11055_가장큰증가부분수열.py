n = int(input())

arr = list(map(int, input().split()))
arr.insert(0, 0)
dp = [0] * (n + 1)
dp[1] = arr[1]

for i in range(2, n+1):

    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + arr[i])
        # else:
        #     dp[i] = max(dp[i], arr[i])


# print(dp)
print(max(dp))
