import sys
from itertools import product

input = sys.stdin.readline


def solution(N, M):

  for i in product(list(range(1, N+1)), repeat=M):
    # print(i)
    print(*i)



if __name__ == '__main__':
  N, M = map(int, input().split())

  solution(N, M)