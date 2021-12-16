import sys
from collections import deque
sys.setrecursionlimit(10**6)
t = int(input())


def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    
    if field[x][y] == 1:
        field[x][y] = 0

        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

for _ in range(t):
    n, m, k = map(int, input().split())
    field = [[0] * m for _ in range(n)]
    ans = 0
    for _ in range(k):
        a, b = map(int, input().split())
        field[a][b] = 1
    
    for i in range(n):
        for j in range(m):
            if dfs(i, j) == True:
                ans += 1

    print(ans)
