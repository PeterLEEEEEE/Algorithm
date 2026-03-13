import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

dy = [-2, -2, 0, 0, 2, 2]
dx = [-1, 1, -2, 2, -1, 1]
r1, c1, r2, c2 = map(int, input().split())
visited = [[0]*N for _ in range(N)]


def bfs(y, x):

    q = deque()
    q.append([y, x])
    
    while q:
        y, x = q.popleft()
        
        for i in range(6):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < N and 0 <= nx < N and visited[ny][nx] == 0:
                visited[ny][nx] = visited[y][x] + 1
                if ny == r2 and nx == c2:
                    return visited[ny][nx]
                
                q.append([ny, nx])
    
    return -1
            

print(bfs(r1, c1))
