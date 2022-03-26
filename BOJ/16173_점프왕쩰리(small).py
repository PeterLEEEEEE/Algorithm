from re import L
import sys
from collections import deque


input = sys.stdin.readline

N = int(input())
g_map = []
dy = [1, 0]
dx = [0, 1]

def bfs(x, y):
    q = deque()
    q.append([y, x])

    visited = [[False]* N for _ in range(N)]

    while q:
        y, x = q.popleft()
        
        move = g_map[y][x]
        if move == -1:
            return True

        for i in range(2):
            ny = y + dy[i] * move
            nx = x + dx[i] * move

            if 0 <= ny < N and 0 <= nx < N and visited[ny][nx] == False:
                visited[ny][nx] = True
                q.append([ny, nx])

    return False

for _ in range(N):
    g_map.append(list(map(int, input().split())))

if bfs(0, 0):
    print('HaruHaru')
else:
    print("Hing")

