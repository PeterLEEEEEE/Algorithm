import sys
from collections import deque


input = sys.stdin.readline
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
N = int(input())
cnt = 0
cnt2 = 0
rb_map = [list(map(str, input().rstrip())) for _ in range(N)]


def bfs(y, x):
    q = deque()
    q.append([y, x])
    
    visited[y][x] = True
    
    while q:
        y, x = q.popleft()
        
        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x

            if 0 <= ny < N and 0 <= nx < N:
                if rb_map[y][x] == rb_map[ny][nx] and visited[ny][nx] == False:
                    visited[ny][nx] = True
                    q.append([ny, nx])
    
visited = [[False]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            bfs(i, j)
            cnt += 1

visited = [[False]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if rb_map[i][j] == 'G':
            rb_map[i][j] = 'R'
for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            bfs(i, j)
            cnt2 += 1
print(cnt, cnt2)