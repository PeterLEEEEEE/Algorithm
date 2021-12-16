from collections import deque


def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if field[nx][ny] != 0:
                continue 

            field[nx][ny] = field[x][y] + 1
            queue.append([nx, ny])


m, n = map(int, input().split())
field = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = 0
queue = deque([])
for _ in range(n):
    field.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if field[i][j] == 1:
            queue.append([i,j])

bfs()
# print(field)
flag = False
for i in field:
    if 0 in i:
        print(-1)
        flag = True
        break
    ans = max(ans, max(i))
if flag == False:
    print(ans - 1)
