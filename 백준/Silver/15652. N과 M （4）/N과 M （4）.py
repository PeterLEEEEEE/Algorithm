import sys
from itertools import combinations_with_replacement

input = sys.stdin.readline


def solution(N, M):

  for i in combinations_with_replacement(list(range(1, N+1)), M):
    print(*i)


if __name__ == '__main__':
  # write input
  N, M = map(int, input().split())
  solution(N, M)