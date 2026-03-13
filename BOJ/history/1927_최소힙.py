import sys
import heapq


input = sys.stdin.readline


def solution():
  pass


if __name__ == '__main__':
  # write input
  N = int(input())
  heap = []
  cnt = 0
  for i in range(N):
    num = int(input())
    if num == 0:
      if heap:
        print(heapq.heappop(heap))
      else:
        print(0)
    else:
      heapq.heappush(heap, num)

