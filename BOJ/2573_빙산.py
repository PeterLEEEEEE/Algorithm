import sys
import copy 
from collections import deque

sys.setrecursionlimit(10**5)
input = sys.stdin.readline

N, M = map(int, input().split())

field = []


dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
year = 0
 

for _ in range(N):
    field.append(list(map(int, input().split())))

def dfs(y, x):
    visited[y][x] = True
    
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < N and 0 <= nx < M and field[ny][nx] != 0:
            if visited[ny][nx] == False:
                dfs(ny, nx)
    
def melt(y, x):
    melt_cnt = 0
    
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < N and 0 <= nx < M and field[ny][nx] == 0:
            if field[y][x] > 0:
                melt_cnt += 1
    
    return melt_cnt

while True:
    year += 1
    ans = 0
    melted_field = [[0]*M for _ in range(N)]
    
    for y in range(N):
        for x in range(M):
            if field[y][x] > 0:
                melted_field[y][x] = melt(y, x)
    
    for y in range(N):
        for x in range(M):
            if field[y][x] - melted_field[y][x] <= 0:
                field[y][x] = 0
            else:
                field[y][x] -= melted_field[y][x]

    visited = [[False]*M for _ in range(N)]
    
    for y in range(N):
        for x in range(M): 
            if field[y][x] != 0 and not visited[y][x]:
                dfs(y, x)
                ans += 1

    if ans > 1:
        print(year)
        break
    elif ans == 0:
        print(0)
        break
    
# print(field)