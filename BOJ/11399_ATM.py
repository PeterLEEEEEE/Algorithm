n = int(input())

arr = list(map(int, input().split()))

arr.sort()

ans = 0

for i in range(1, len(arr)+1):
    for j in range(0, i):
        ans += arr[j]

print(ans)