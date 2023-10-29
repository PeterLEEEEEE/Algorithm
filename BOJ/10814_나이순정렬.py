import sys


input = sys.stdin.readline


def solution():
  pass


if __name__ == '__main__':
  # write input
  N = int(input())
  arr = []

  for i in range(N):
    age, name = map(str, input().split())
    arr.append([int(age), name])

  ans = sorted(arr, key=lambda x: x[0])

  for i in ans:
    print(i[0], i[1])