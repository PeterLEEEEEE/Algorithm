import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
a, b = map(int, input().split())
cnt = N

for i in range(len(arr)):
    arr[i] = arr[i] - a
    if arr[i] > 0:
        temp = arr[i] // b
        if arr[i] % b == 0:
            cnt += temp
        else:
            cnt += (temp + 1)

print(cnt)
