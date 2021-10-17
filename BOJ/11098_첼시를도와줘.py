def sol(arr):

    temp = []
    for i in arr:
        cost, player = i.split()
        temp.append([int(cost), player])

    return sorted(temp, key=lambda x: -x[0])[0][1]


if __name__ == "__main__":
    n = int(input())

    for _ in range(n):
        arr = []
        nn = int(input())
        for _ in range(nn):
            arr.append(input())

        print(sol(arr))
