import sys


input = sys.stdin.readline

R, C = map(int, input().split())

board = [list(map(str, input().rstrip())) for _ in range(R)]
ans = 0
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
temp = set()


def dfs(y, x, cnt):
    global ans
    
    ans = max(cnt, ans)
    
    for i in range(4):
        ny = dy[i] + y
        nx = dx[i] + x
        
        if 0 <= ny < R and 0 <= nx < C and board[ny][nx] not in temp:
            temp.add(board[ny][nx])
            dfs(ny, nx, cnt+1)
            temp.remove(board[ny][nx])

temp.add(board[0][0])
dfs(0, 0, 1)

print(ans)