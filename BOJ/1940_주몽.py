import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
arr = list(map(int, input().split()))
arr.sort()

ans = 0
start = 0
end = len(arr) - 1

while start < end:
    if arr[start] + arr[end] == M:
        ans += 1
        start += 1
        end -= 1
    elif arr[start] + arr[end] < M:
        start += 1
    else:
        end -= 1

print(ans)