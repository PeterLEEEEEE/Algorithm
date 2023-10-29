# dfs로 풀면 메모리 초과남
import sys
from collections import deque

input = sys.stdin.readline


n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
painting_cnt = 0
max_cnt = 0
temp = 0

dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]


# def dfs(y, x, temp):
#   temp += 1

#   for i in range(4):
#     ny = dy[i] + y
#     nx = dx[i] + x

#     if 0 <= ny < n and 0 <= nx < m and arr[ny][nx] != 0:
#       arr[ny][nx] = 0
#       temp = dfs(ny, nx, temp)

#   return temp

def bfs(y, x):
  cnt = 1

  queue = deque()
  queue.append([y, x])
  while queue:
    y, x = queue.popleft()

    for i in range(4):
      ny = dy[i] + y
      nx = dx[i] + x

      if 0 <= ny < n and 0 <= nx < m and arr[ny][nx] == 1:
        if visited[ny][nx] == False:
          visited[ny][nx] = True
          cnt += 1
          queue.append([ny, nx])

  return cnt

for i in range(n):
  for j in range(m):

    # if arr[i][j] == 1:
    #     arr[i][j] = 0
    #     painting_cnt += 1
    #     temp = dfs(i, j, temp)
    # max_cnt = max(max_cnt, temp)
    if arr[i][j] == 1 and visited[i][j] == False:
      visited[i][j] = True
      painting_cnt += 1
      temp = bfs(i, j)
    max_cnt = max(max_cnt, temp)

print(painting_cnt)
print(max_cnt)