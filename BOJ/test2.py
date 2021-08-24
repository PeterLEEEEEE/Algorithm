def top(nums, k):
    if not nums:
        return []
    elif len(nums) == 1:
        return nums
    
    arr = []
    maxnum = 0
    for i in set(nums):
        arr.append([i, nums.count(i)])
    
    arr.sort(key=lambda x: -x[1])
    
    print(arr)


k = 2
nums = [1,1,2,2,2,2,3,3,3]
top(nums, k)











# n = int(input())

# arr = list(map(int, input().split()))

# dp = [1] * n

# for i in range(1, len(dp)):
#     if arr[i] > max(arr[:i]):
#         dp[i] = max(dp) + 1

# print(max(dp))