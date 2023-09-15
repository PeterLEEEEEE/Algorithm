import sys
from itertools import permutations

input = sys.stdin.readline


def solution(arr, M):
  arr.sort()
  ans_list = []
  for i in permutations(arr, M):
    ans_list.append(list(i))

  # ans_list.sort(key=lambda x: (x[0], x[1]))
  for ans in ans_list:
    print(*ans)

if __name__ == '__main__':
  # write input
  N, M = map(int, input().split())
  arr = list(map(int, input().split()))
  solution(arr, M)