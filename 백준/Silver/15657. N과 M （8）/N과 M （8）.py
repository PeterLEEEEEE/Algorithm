import sys
from itertools import combinations_with_replacement

input = sys.stdin.readline


def solution(arr):
  for i in combinations_with_replacement(arr, M):
    print(*list(i))


if __name__ == '__main__':
  # write input
  N, M = map(int, input().split())

  arr = list(map(int, input().split()))
  arr.sort()
  solution(arr)