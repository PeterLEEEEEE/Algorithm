import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
checker = [[0] * M for _ in range(N)]

dy = [0, 0, -1, 1, -1, 1, -1, 1]
dx = [-1, 1, 0, 0, -1, 1, 1, -1]
queue = deque()

for y in range(N):
  for x in range(M):
    if arr[y][x] == 1:
      queue.append([y,x])

while queue:
  y, x = queue.popleft()

  for i in range(8):
    ny = dy[i] + y
    nx = dx[i] + x

    if 0 <= ny < N and 0 <= nx < M:
      if arr[ny][nx] == 0:
        arr[ny][nx] = arr[y][x] + 1
        queue.append([ny, nx])

ans = 0
for y in range(N):
  for x in range(M):
    ans = max(ans, arr[y][x])

print(ans-1)