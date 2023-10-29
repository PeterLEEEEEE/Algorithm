import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
  N = int(input())
  queue = deque()
  arr = list(map(int, input().split()))
  arr.sort(reverse=True)

  i = 0
  while i < len(arr):
    if i == 0 or i % 2 == 0:
      queue.append(arr[i])
    else:
      queue.appendleft(arr[i])

    i += 1

  max_val = 0
  for i in range(len(arr)-1):
    max_val = max(max_val, abs(queue[i]-queue[i+1]))

  print(max_val)