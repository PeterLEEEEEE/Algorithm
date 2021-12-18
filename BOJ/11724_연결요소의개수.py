import sys
sys.setrecursionlimit(10000)
N, M = map(int, input().split())

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
            
        
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
ans = 0
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for g in graph:
    g.sort()

# print(graph)
# dfs(1)

for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        ans += 1
print(ans)