import sys 
sys.setrecursionlimit(10000)

def dfs(y, x, new_map, points):
    new_map[y][x] = 'X'
    dy = [0, 0, -1, 1]
    dx = [1, -1, 0, 0]

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

    for y in range(len(new_map)):
        for x in range(len(new_map[0])):
            if new_map[y][x] != 'X':
                answer.append(dfs(y, x, new_map, int(new_map[y][x])))

    if not answer:
        answer.append(-1)

    return sorted(answer)
