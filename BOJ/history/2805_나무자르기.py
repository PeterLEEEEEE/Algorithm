import sys


input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

start = 1
end = sum(arr)

while start <= end:
    mid = (start + end) // 2
    val_sum = 0

    for val in arr:
        if val > mid:
            val_sum += (val - mid)
    
    if val_sum >= M:
        start = mid + 1
    
    else:
        end = mid - 1

print(end)

