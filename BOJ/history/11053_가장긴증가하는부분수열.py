'''
dp 문제, 역시나 어려우니 적응될 때까지 매일 풀어보기

'''

n = int(input())
arr = list(map(int, input().split()))

dp = [1] * n


for i in range(1, n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))


##############################################
# 원래 답안

# n = int(input())

# nums = [0]
# dp = [0] * (n+1)
# dp[1] = 1


# nums.extend(list(map(int, input().split())))

# for i in range(2, n+1):
#     maxlen = 0
#     for j in range(i-1, 0, -1):
#         if nums[j] < nums[i] and dp[j] > maxlen:
#             maxlen = dp[j]
#         dp[i] = maxlen+1


# print(max(dp))
