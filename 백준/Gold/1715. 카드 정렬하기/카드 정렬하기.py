import sys
import heapq

input = sys.stdin.readline

N = int(input())

arr = []
ans = 0

for _ in range(N):
  heapq.heappush(arr, int(input()))

if len(arr) == 0:
  print(ans)
else:
  for i in range(N-1):
    prev = heapq.heappop(arr)
    cur = heapq.heappop(arr)

    ans += (prev + cur)
    heapq.heappush(arr, prev + cur)

  print(ans)