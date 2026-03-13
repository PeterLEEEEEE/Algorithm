n = int(input())

for _ in range(n):
    arr = input().split()
    for i in arr:
        print(i[::-1], end = ' ')