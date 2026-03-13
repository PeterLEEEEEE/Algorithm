import sys


input = sys.stdin.readline


def solution(n):
  dp = [0] * (n+2)
  dp[1] = 1
  dp[2] = 2

  if n == 1 or n == 2:
    return dp[n]

  for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]

  return dp[n] % 10007

if __name__ == '__main__':
  # write input
  n = int(input())
  print(solution(n)) if n != 0 else print(0)
