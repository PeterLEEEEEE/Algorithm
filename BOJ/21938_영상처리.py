import sys
from collections import deque


input = sys.stdin.readline
rgb_map = []
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def bfs(y, x):
    q = deque()
    q.append([y, x])
    visited[y][x] = True

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < N and 0 <= nx < M:
                if visited[ny][nx] == False and rgb_map[ny][nx] >= (T*3):
                    visited[ny][nx] = True
                    q.append([ny, nx])


N, M = map(int, input().split())
visited = [[False]*M for _ in range(N)]
ans = 0

for _ in range(N):
    sum_list = list(map(int, input().split()))
    arr = []
    
    for i in range(M):
        arr.append(sum(sum_list[3*i:3*(i+1)]))

    rgb_map.append(arr)
        
T = int(input())

for i in range(N):
    for j in range(M):
        if rgb_map[i][j] >= (T*3) and visited[i][j] == False:
            bfs(i, j)
            ans += 1

print(ans)