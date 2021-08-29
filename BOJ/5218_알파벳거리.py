n = int(input())

for _ in range(n):
    arr = []
    arr = input().split()

    print('Distances: ', end='')
    for i in range(len(arr[0])):
        x = ord(arr[0][i])
        y = ord(arr[1][i])
        if y >= x:
            distance = y - x
        else:
            distance = y + 26 - x
        print(distance, end=' ')
    print()
