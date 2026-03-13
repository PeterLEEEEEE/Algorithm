import sys

input = sys.stdin.readline

N = int(input())
dp = [[0, []] for _ in range(N + 1)]
dp[1][0] = 0
dp[1][1] = [1]
dp[2][0] = 1
dp[2][1] = [1, 2]

for i in range(3, N + 1):
    
    dp[i][0] = dp[i-1][0] + 1
    dp[i][1] = dp[i-1][1] + [i]
    
    if i % 3 == 0 and dp[i//3][0] + 1 < dp[i][0]:
        dp[i][0] = dp[i // 3][0] + 1
        dp[i][1] = dp[i // 3][1] + [i]
    
    if i % 2 == 0 and dp[i//2][0] + 1 < dp[i][0]:
        dp[i][0] = dp[i // 2][0] + 1
        dp[i][1] = dp[i // 2][1] + [i]
    

print(dp[N][0])
print(*dp[N][1][::-1])
# print(dp)

# ans = []
# cnt = 0

# temp = N
# while N != 1:
    
#     if N % 3 == 0:
#         N //= 3
    
#     elif (N - 1) % 3 == 0:
#         N -= 1
    
#     elif (N - 1) % 2 == 0:
#         N -= 1
    
#     elif N % 2 == 0:
#         N //= 2
    
#     ans.append(N)
#     cnt += 1

# print(cnt)
# print(temp, *ans)

# dp[1] = 0
# dp[2] = 1
# dp[3] = 1
# dp[4] = 2
# dp[5] = 3
# dp[6] = 2
# dp[7] = 3
# dp[8] = 3
# dp[9] = 3
# dp[10] = 3
# dp[11] = 4
# dp[12] = 3
# dp[13] = 4