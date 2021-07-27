import sys
n = int(input())
arr = []

for _ in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))
    # arr.append([list(map(int, input().split()))])


arr.sort(key=lambda x: x[0])

dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if arr[i][1] > arr[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))