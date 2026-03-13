from collections import deque
import sys
import copy
from collections import deque

input = sys.stdin.readline

R, C ,N = map(int, input().split())
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
field = [list(input().rstrip()) for _ in range(R)]
bomb = deque()

def bomb_cord():
    for y in range(R):
        for x in range(C):
            if field[y][x] == 'O':
                bomb.append([y, x])

def plantbomb_all():
    for y in range(R):
        for x in range(C):
            if field[y][x] != 'O':
                field[y][x] = 'O'

def explode():
    while bomb:
        y, x = bomb.popleft()
        field[y][x] = '.'
        
        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x
            if 0 <= ny < R and 0 <= nx < C and field[ny][nx] == 'O':
                field[ny][nx] = '.'

def time_check(N):
    if N == 0:
        return True
    return False


N -= 1
while N > 0:
    bomb_cord()
    plantbomb_all()
    N -= 1
    if time_check(N):
        break
    
    explode()
    
    N -= 1

for i in field:
    print(''.join(i))
    
    

