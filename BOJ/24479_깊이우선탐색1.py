import sys


sys.setrecursionlimit(10**9)
input = sys.stdin.readline


N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
cnt = 1

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    

def dfs(R):
    visited[R] = cnt
    graph[R].sort()
    
    for i in graph[R]:
        if visited[i] == 0:
            cnt += 1
            dfs(i)
    
dfs(R, cnt)

for i in range(1, N+1):
    print(visited[i])