# O(n) 미친.. 이런 방법이 

n = int(input())

arr = list(map(int, input().split()))

dp = [0] * n
dp[0] = arr[0]

for i in range(1, n):
    dp[i] = max(0, dp[i-1]) + arr[i]


print(max(dp))




# O(n^2) 방식(메모리 초과 뜸 ㅜ)
# n = int(input())

# arr = list(map(int, input().split()))

# dp = [[0] * n for _ in range(n)]
# dp[0][0] = arr[0]
# ans = 0

# # for i in range(n):
# #     if i <= 0:
# #         continue
# #     for j in range(i+1, n):
# #         dp[i][j] = arr[j] + dp[i][j-1]
# #     ans = max(ans, max(dp[i]))

# print(ans)