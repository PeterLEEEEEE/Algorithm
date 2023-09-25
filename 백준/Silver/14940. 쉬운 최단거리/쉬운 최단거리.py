import sys
from collections import deque

input = sys.stdin.readline

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

flag = 0

def solution(y, x):

  queue = deque()
  queue.append([y,x])

  while queue:
    y, x = queue.popleft()

    for i in range(4):
      ny = dy[i] + y
      nx = dx[i] + x

      if 0 <= ny < n and 0 <= nx < m and visited[ny][nx] == False:
        if arr[ny][nx] != 0:
          visited[ny][nx] = True
          arr[ny][nx] = arr[y][x]+1
          queue.append([ny, nx])



if __name__ == '__main__':
  # write input
  n, m  = map(int, input().split())

  arr = [list(map(int, input().split())) for _ in range(n)]
  visited = [[False] * m for _ in range(n)]

  for y in range(n):
    for x in range(m):
      if arr[y][x] == 2:
        flag = 1
        arr[y][x] = 0
        visited[y][x] = True
        solution(y, x)

      if flag == 1:
        break
    if flag == 1:
      break

  # for y in range(n):
  #   for x in range(m):
  #     if arr[y][x] == 1 and visited[y][x] == 0:
  #       visited[y][x] = -1

  for y in range(n):
    for x in range(m):
      if visited[y][x] == False and arr[y][x] != 0:
        print(-1, end=" ")
      else:
        print(arr[y][x], end=" ")
    print()