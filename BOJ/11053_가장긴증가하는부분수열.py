'''
dp 문제, 역시나 어려우니 적응될 때까지 매일 풀어보기

'''

n = int(input())

nums = [0]
dp = [0] * (n+1)
dp[1] = 1

# nums.insert(0,0) 이렇게 앞에 0을 0번 인덱스에 넣는 방식을 사용해도 무방함
nums.extend(list(map(int, input().split())))

for i in range(2, n+1):
    maxlen = 0
    for j in range(i-1, 0, -1):
        if nums[j] < nums[i] and dp[j] > maxlen:
            maxlen = dp[j]
        dp[i] = maxlen+1


print(max(dp))
