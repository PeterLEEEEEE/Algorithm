import sys
from collections import deque

input = sys.stdin.readline

M, N, H = map(int, input().split())

arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

dy = [0, 0, 1, 0, -1, 0]
dx = [0, 0, 0, 1, 0, -1]
dz = [1, -1, 0, 0, 0, 0]
zero_flag = 0
zero_exists = 0
ans = 0
queue = deque()


def sol(queue):

  while queue:
    z, y, x = queue.popleft()

    for i in range(6):
      ny = dy[i] + y
      nx = dx[i] + x
      nz = dz[i] + z

      if 0 <= ny < N and 0 <= nx < M and 0 <= nz < H and arr[nz][ny][nx] == 0:
        arr[nz][ny][nx] = arr[z][y][x] + 1
        queue.append([nz, ny, nx])


for z in range(H):
  for y in range(N):
    for x in range(M):
      if arr[z][y][x] == 1:
        queue.append([z, y, x])

if zero_flag == 1:
  print(0)
else:
  sol(queue)

  for z in range(H):
    if zero_exists == 1:
      break
    for y in range(N):
      if zero_exists == 1:
        break
      for x in range(M):
        if arr[z][y][x] == 0:
          zero_exists = 1
          break
        else:
          ans = max(ans, arr[z][y][x])
  if zero_exists:
    print(-1)
  else:
    print(ans-1)
