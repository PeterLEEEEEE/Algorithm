import sys
from itertools import combinations

input = sys.stdin.readline

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
temp = list(range(N))
ans = sys.maxsize

for r1 in combinations(temp, N//2):
  start, link = 0, 0
  r2 = list(set(temp) - set(r1))

  for r in combinations(r1, 2):
    start += (arr[r[0]][r[1]] + arr[r[1]][r[0]])
  for r in combinations(r2, 2):
    link += (arr[r[0]][r[1]] + arr[r[1]][r[0]])

  ans = min(ans, abs(start-link))

print(ans)
