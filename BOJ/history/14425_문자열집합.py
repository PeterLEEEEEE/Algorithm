N, M = map(int, input().split())
arr1, arr2 = [], []
cnt = 0

for _ in range(N):
    arr1.append(input())
for _ in range(M):
    arr2.append(input())

for item in arr2:
    if item in arr1:
        cnt += 1

print(cnt)