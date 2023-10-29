import sys
from collections import deque

input = sys.stdin.readline

t = int(input())


dy = [-2, -1, 2, 1, -1, -2, 1, 2]
dx = [-1, -2, 1, 2, 2, 1, -2, -1]

def bfs(y, x):

  queue = deque()
  queue.append([y, x])

  while queue:
    y, x = queue.popleft()
    if y == targetY and x == targetX:
      return arr[y][x] - 1

    for i in range(8):
      ny = dy[i] + y
      nx = dx[i] + x

      if 0 <= ny < n and 0 <= nx < n and arr[ny][nx] == 0:
        arr[ny][nx] = arr[y][x] + 1
        queue.append([ny, nx])

  return 0

for _ in range(t):
  n = int(input())
  arr = [[0]* n for _ in range(n)]
  startX, startY = map(int, input().split())
  targetX, targetY = map(int, input().split())
  arr[startY][startX] = 1
  move = bfs(startY, startX)

  print(move)
