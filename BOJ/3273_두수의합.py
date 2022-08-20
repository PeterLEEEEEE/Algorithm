import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
x = int(input())
arr.sort()
start = 0
end = n - 1
cnt = 0

while start < end:
    if arr[start] + arr[end] == x:
        cnt += 1
        start += 1
        end -= 1
    elif arr[start] + arr[end] > x:
        end -= 1
    else:
        start += 1

print(cnt)