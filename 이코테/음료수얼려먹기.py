
def DFS(x,y,graph):
    if x < 0 or y < 0 or x >= N or y >= M:
        return False
    
    if graph[x][y] == 0:
        graph[x][y] = 1
    
        DFS(x-1, y, graph)
        DFS(x+1, y, graph)
        DFS(x, y-1, graph)
        DFS(x, y+1, graph)
        return True
    return False



N, M = map(int, input().split())
ans = 0
graph = []
for _ in range(N):
    graph.append(list(map(int, input())))

for i in range(N):
    for j in range(M):
        if DFS(i, j, graph) == True:
            ans += 1

print(ans)

