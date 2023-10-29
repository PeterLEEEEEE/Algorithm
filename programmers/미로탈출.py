from collections import deque

def bfs(startY, startX, endY, endX, maps):
  visited = [[False] * len(list(maps[0])) for _ in range(len(maps))]
  visited[startY][startX] = True
  dy = [0, 0, 1, -1]
  dx = [1, -1, 0, 0]
  queue = deque()
  queue.append([startY, startX, 0])

  while queue:
    y, x, cost = queue.popleft()

    if maps[y][x] == maps[endY][endX]:
      return cost

    for i in range(4):
      ny = y + dy[i]
      nx = x + dx[i]

      if 0 <= ny < len(maps) and 0 <= nx < len(maps[0]) and maps[ny][nx] != 'X':
        if not visited[ny][nx]:
          queue.append([ny, nx, cost+1])
          visited[ny][nx] = True

  return -1

def solution(maps):
  answer = 0
  startY, startX, leverY, leverX, endY, endX = 0, 0, 0, 0, 0, 0

  for y in range(len(maps)):
    for x in range(len(maps[0])):
      if maps[y][x] == 'S':
        startY, startX = y, x
      if maps[y][x] == 'L':
        leverY, leverX = y, x
      if maps[y][x] == 'E':
        endY, endX = y, x

  startToLever = bfs(startY, startX, leverY, leverX, maps)
  leverToEnd = bfs(leverY, leverX, endY, endX, maps)

  if startToLever == -1 or leverToEnd == -1:
    return -1
  return startToLever + leverToEnd


maps = ["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]

print(solution(maps))