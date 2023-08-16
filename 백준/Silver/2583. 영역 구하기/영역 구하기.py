import sys
from collections import deque

input = sys.stdin.readline

M, N, K = map(int, input().split())
arr = [[1] * N for _ in range(M)]
dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

for _ in range(K):
  x1, y1, x2, y2 = map(int, input().split())

  for y in range(y1, y2):
    for x in range(x1, x2):
      arr[y][x] = 0

def bfs(y, x):
  cnt = 1
  queue = deque()
  queue.append([y,x])

  while queue:
    y, x = queue.popleft()

    for i in range(4):
      ny = dy[i] + y
      nx = dx[i] + x

      if 0 <= ny < M and 0 <= nx < N and arr[ny][nx] == 1:
        cnt += 1
        arr[ny][nx] = 0
        queue.append([ny, nx])

  return cnt

ans1 = 0
ans = []
for y in range(M):
  for x in range(N):
    if arr[y][x] == 1:
      ans1 += 1
      arr[y][x] = 0
      ans.append(bfs(y, x))

print(ans1)
print(*sorted(ans))