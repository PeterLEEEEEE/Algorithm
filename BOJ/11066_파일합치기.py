# 모르겠다 못풀겠다

n = int(input())

for _ in range(n):

    arr = []

    k = int(input())
    dp = [0] * (k+1)

    arr = list(map(int, input().split()))

    arr.sort()

    for i in range(0, len(arr), 2):
        dp.append(dp[-1] + arr[i]+arr[i+1])

    print(dp)
