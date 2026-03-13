import sys

input = sys.stdin.readline

N, M = map(int, input().split())
t_map = []
visited = [[False]*M for _ in range(N)]
ans = 0

def dfs(t_map, visited, i, j, target):
    
    if 0 <= i < N and 0 <= j < M:
        temp = t_map[i][j]

        if visited[i][j] == True:
            return
        if target == temp:
            visited[i][j] = True
        if temp == '-':
            dfs(t_map, visited, i, j+1, temp)
        elif temp == '|':
            dfs(t_map, visited, i+1, j, temp)
    else:
        return


for _ in range(N):
    t_map.append(input().rstrip())


for i in range(N):
    for j in range(M):
        if visited[i][j] == False:
            temp = t_map[i][j]
            dfs(t_map, visited, i, j, temp)
            ans += 1

print(ans)
