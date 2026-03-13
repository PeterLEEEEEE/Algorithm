from operator import xor
import sys, copy
from collections import deque


input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
max_space = 0
cnt = 0


def bfs():
    global max_space

    lab_copy = copy.deepcopy(lab_list)
    q = deque()
    
    for i in range(N):
        for j in range(M):
            if lab_copy[i][j] == 2:
                q.append([i, j])
    while q:
        y, x = q.popleft()
        for i in range(4):
        
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 0 <= ny < N and 0 <= nx < M:
                if lab_copy[ny][nx] == 0:
                    lab_copy[ny][nx] = 2
                    q.append([ny, nx])
    
    room = 0
    
    for i in range(N):
        for j in range(M):
            if lab_copy[i][j] == 0:
                room += 1
    

    max_space = max(room, max_space)


def set_wall(cnt):
    if cnt == 3:
        bfs()
        return 

    for i in range(N):
        for j in range(M):
            if lab_list[i][j] == 0:
                lab_list[i][j] = 1
                
                set_wall(cnt + 1)

                lab_list[i][j] = 0


N, M = map(int, input().split())
lab_list = [list(map(int, input().split())) for _ in range(N)]


set_wall(cnt)


print(max_space)
