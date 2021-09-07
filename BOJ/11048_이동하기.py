n, m = map(int, input().split())

arr = []


for _ in range(n):
    arr.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            arr[i][j] = arr[i][j]
        elif i == 0 and j > 0:
            arr[i][j] += arr[i][j-1]
        elif i > 0 and j == 0:
            arr[i][j] += arr[i-1][j]
        elif i > 0 and j > 0:
            arr[i][j] += max(arr[i-1][j-1], arr[i-1][j], arr[i][j-1])

print(arr[-1][-1])
