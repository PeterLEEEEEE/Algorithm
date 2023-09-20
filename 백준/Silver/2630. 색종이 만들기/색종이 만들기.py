import sys

def sol(x,y,N):
    global white, blue
    start = mat[x][y]
    flag = True
    for i in range(x, x+N):
        if not flag:
            break
        for j in range(y, y+N):
            if start != mat[i][j]:
                flag = False
                sol(x, y, N//2)
                sol(x, y+(N//2), N//2)
                sol(x+(N//2), y, N//2)
                sol(x+(N//2), y+(N//2), N//2)
                break
    if flag:
        if start:
            blue += 1
        else:
            white += 1

input = sys.stdin.readline
N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]


white, blue = 0, 0
sol(0,0,N)
print(white, blue, sep='\n')
