import sys

input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
arr.sort()

start = 0
end = len(arr) - 1
target = 0
diff = float('inf')
ans = []

while start < end:
    cur = arr[end] + arr[start]
    
    if abs(cur) < diff:
        diff = abs(cur)
        ans = [arr[start], arr[end]]
    
    if cur > 0:
        end -= 1
    else:
        start += 1

print(*ans)