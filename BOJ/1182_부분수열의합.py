import sys
from itertools import combinations

input = sys.stdin.readline

N, S = map(int, input().split())

arr = list(map(int, input().split()))
ans = 0

for i in range(1, N+1):
  temp = combinations(arr, i)

  for i in temp:
    if sum(i) == S:
      ans += 1

print(ans)