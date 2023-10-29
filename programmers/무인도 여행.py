
def dfs(y, x, new_map, points):
  new_map[y][x] = 'X'
  dx = [0, 0, -1, 1]
  dy = [1, -1, 0, 0]

  for i in range(4):
    ny = dy[i] + y
    nx = dx[i] + x

    if ny >= 0 and ny < len(new_map) and nx >= 0 and nx < len(new_map[0]):
      if new_map[ny][nx] != 'X':

        points = dfs(ny, nx, new_map, points + int(new_map[ny][nx]))

  return points

def solution(maps):
  answer = []
  new_map = []
  for row in maps:
    new_map.append(list(row))

  print(new_map)
  for y in range(len(new_map)):
    for x in range(len(new_map[0])):
      if new_map[y][x] != 'X':
        answer.append(dfs(y, x, new_map, int(new_map[y][x])))

  if not answer:
    answer.append(-1)

  return sorted(answer)

maps = ["X591X","X1X5X","X231X", "1XXX1"]


print(solution(maps))