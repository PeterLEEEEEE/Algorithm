import sys
from collections import deque

input = sys.stdin.readline


def dfs(V):
    print(V, end = ' ')
    visited[V] = True
    for i in graph[V]:
        if not visited[i]:
            dfs(i)

def bfs(V):
    visited[V] = True
    queue = deque([V])
    
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

    # graph[a] = graph.get(a, []) + [b]
    # graph[b] = graph.get(b, []) + [a]

for i in range(1, N+1):
    graph[i].sort()

dfs(V)

visited = [False] * (N+1)
print()
bfs(V)
