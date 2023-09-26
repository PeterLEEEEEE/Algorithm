import sys


input = sys.stdin.readline


def solution(n):
    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().split())))

    if n == 1:
        print(*arr[0])
        return

    dp = [[0]*i for i in range(1, n+1)]
    dp[0][0] = arr[0][0]
    dp[1][0] = arr[1][0] + dp[0][0]
    dp[1][1] = arr[1][1] + dp[0][0]


    for i in range(2, n):
        for j in range(len(arr[i])):
            if j == 0:
                dp[i][0] = dp[i-1][0] + arr[i][0]
            elif j == len(arr[i]) - 1:
                dp[i][j] = dp[i-1][j-1] + arr[i][j]
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + arr[i][j]
    # for j in range(len(arr[i])):

    print(max(dp[-1]))


if __name__ == '__main__':
    # write input
    n = int(input())

    solution(n)