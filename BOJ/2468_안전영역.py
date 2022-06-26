import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
land = [list(map(int, input().split())) for _ in range(N)]
max_height = 0
max_cnt = 0

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

for i in range(N):
    max_height = max(max_height, max(land[i]))



def bfs(y, x, height):
    q = deque()
    q.append([y, x])
    visited[y][x] = True

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x

            if 0 <= ny < N and 0 <= nx < N and land[ny][nx] >= height:
                if visited[ny][nx] == False:
                    visited[ny][nx] = True
                    q.append([ny, nx])


for h in range(1, 100):
    cnt = 0
    visited = [[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if land[i][j] < h:
                visited[i][j] = True
            if visited[i][j] == False:
                bfs(i, j, h)
                cnt += 1

    max_cnt = max(max_cnt, cnt)

print(max_cnt)