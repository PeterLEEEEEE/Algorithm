import sys
from collections import deque

input = sys.stdin.readline

N, M, K = map(int, input().split())
arr = [[0] * M for _ in range(N)]
max_cnt = 0
dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]


def bfs(y, x):

  queue = deque()
  queue.append([y,x])
  gc = 0

  while queue:
    y, x = queue.popleft()
    gc += 1
    for i in range(4):
      ny = dy[i] + y
      nx = dx[i] + x
      if 0 <= ny < N and 0 <= nx < M and arr[ny][nx] == 1:
        queue.append([ny, nx])
        arr[ny][nx] = 0
  return gc

for _ in range(K):
  y, x = map(int, input().split())
  arr[y-1][x-1] = 1

for i in range(N):
  for j in range(M):
    if arr[i][j] == 1:
      arr[i][j] = 0
      cnt = bfs(i, j)

      max_cnt = max(cnt, max_cnt)

print(max_cnt)