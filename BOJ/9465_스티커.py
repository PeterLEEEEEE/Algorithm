import sys


input = sys.stdin.readline


def solution(n):

    for _ in range(n):
        arr = []
        column = int(input())
        for _ in range(2):
            arr.append(list(map(int, input().split())))
        if column == 1:
            print(max(arr[0][0], arr[1][0]))
            continue

        dp = [[0] * (column) for _ in range(2)]

        dp[0][0] = arr[0][0]
        dp[1][0] = arr[1][0]
        dp[1][1] = arr[1][1] + dp[0][0]
        dp[0][1] = arr[0][1] + dp[1][0]

        for i in range(2, column):
            dp[0][i] = arr[0][i] + max(dp[1][i-1], dp[1][i-2])
            dp[1][i] = arr[1][i] + max(dp[0][i-1], dp[0][i-2])

        print(max(dp[0][-1], dp[1][-1]))


if __name__ == '__main__':
  # write input
    n = int(input())

    solution(n)