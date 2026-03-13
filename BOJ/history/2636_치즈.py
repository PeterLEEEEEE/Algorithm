import sys
from collections import deque

input = sys.stdin.readline

r, c = map(int, input().split())

field = []
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

for _ in range(r):
    field.append(list(map(int, input().split())))

def move():
    queue = deque()
    queue.append([0, 0])
    melt_cnt = 0
    visited = [[False] * c for _ in range(r)]
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x
            
            if 0 <= ny < r and 0 <= nx < c:
                if field[ny][nx] == 0 and visited[ny][nx] == False:
                    visited[ny][nx] = True
                    queue.append([ny,nx])

                elif field[ny][nx] == 1:
                    visited[ny][nx] = True
                    field[ny][nx] = 0
                    melt_cnt += 1
                    
    return melt_cnt

melt_hist = []

while True:
    melt_cnt = move()

    if melt_cnt == 0:
        break

    melt_hist.append(melt_cnt)

print(len(melt_hist))
print(melt_hist[-1])