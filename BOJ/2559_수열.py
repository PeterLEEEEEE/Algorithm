import sys
input = sys.stdin.readline
n, k = map(int, input().split())

arr = list(map(int, input().split()))

target = sum(arr[:k])
max_num = target
for i in range(len(arr)-k):
    target = target - arr[i] + arr[i+k]
    if target > max_num:
        max_num = target
    

print(max_num)