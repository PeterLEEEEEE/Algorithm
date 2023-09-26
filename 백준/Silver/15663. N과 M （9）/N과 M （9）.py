import sys
from itertools import permutations

input = sys.stdin.readline


def solution(arr):
  ans = set()
  for i in permutations(arr, M):
    ans.add(i)
  if M > 1:
    ans = sorted(list(ans), key=lambda x: (x[0], x[1]))
  else:
    ans = sorted(list(ans), key=lambda x: x[0])
  for i in ans:
    print(*i)
if __name__ == '__main__':
  # write input
  N, M = map(int, input().split())
  arr = list(map(int, input().split()))

  arr.sort()
  solution(arr)