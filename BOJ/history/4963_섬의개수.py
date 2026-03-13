import sys 
input = sys.stdin.readline
sys.setrecursionlimit(10000)

dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, 1, 1, -1]
result = []

def dfs(x, y):
    if x < 0 or y < 0 or x >= h or y >= w:
        return 
    if island[x][y] == 0:
        return
    
    island[x][y] = 0

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        dfs(nx, ny)
    

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    island = []
    cnt = 0
    for _ in range(h):
        island.append(list(map(int, input().split())))
    
    for i in range(h):
        for j in range(w):
            if island[i][j] == 1:
                dfs(i,j)
                cnt += 1
    
    result.append(cnt)

print(*result, sep='\n')