import sys


input = sys.stdin.readline

K = int(input())


dp = [[0, 0] for _ in range(46)]  
dp[1] = [0, 1]
dp[2] = [1, 1]
dp[3] = [1, 2]
dp[4] = [2, 3]

if 1 <= K <= 4:
    print(dp[K][0], dp[K][1])
else:
    for i in range(5, K+1):
        dp[i][0] = dp[i-1][0] + dp[i-2][0]
        dp[i][1] = dp[i-1][1] + dp[i-2][1]
        

    print(dp[K][0], dp[K][1])
