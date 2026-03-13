import sys


input = sys.stdin.readline


def solution():
  pass


if __name__ == '__main__':
  # write input
  N = int(input())
  arr = [int(input()) for _ in range(N)]

  print(*sorted(arr))