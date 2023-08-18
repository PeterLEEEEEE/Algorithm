import sys
from collections import deque

input = sys.stdin.readline

col, row = map(int, input().split())
arr = []
dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

for _ in range(col):
  arr.append(list(input().rstrip()))


def bfs(y, x):
  queue = deque()
  queue.append([y,x])
  f_dist = [[0] * row for _ in range(col)]
  f_dist[y][x] = 1
  cnt = 0
  while queue:
    y, x = queue.popleft()

    for i in range(4):
      ny = dy[i] + y
      nx = dx[i] + x

      if 0 <= ny < col and 0 <= nx < row and arr[ny][nx] == "L" and f_dist[ny][nx] == 0:
        f_dist[ny][nx] = f_dist[y][x] + 1
        cnt = max(cnt, f_dist[ny][nx])
        queue.append([ny, nx])
  return cnt-1

ans = 0
for y in range(col):
  for x in range(row):
    if arr[y][x] == 'L':
      ans = max(ans, bfs(y, x))

print(ans)