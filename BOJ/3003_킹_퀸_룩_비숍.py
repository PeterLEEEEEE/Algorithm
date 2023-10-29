import sys

input = sys.stdin.readline

chess = [1, 1, 2, 2, 2, 8]
arr = list(map(int, input().split()))
ans = []

for i in range(len(chess)):
    ans.append(chess[i] - arr[i])

print(*ans)