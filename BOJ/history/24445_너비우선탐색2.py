import sys
from collections import deque

input = sys.stdin.readline

N, M, R = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)

cnt = 1
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


for i in range(N+1):
    graph[i].sort(reverse=True)

def bfs(node, cnt):
    visited[node] = cnt
    
    
    q = deque()
    q.append(node)
    while q:
        temp = q.popleft()
        for i in graph[temp]:
            if visited[i] == 0:
                cnt += 1
                visited[i] = cnt
                
                q.append(i)

    for i in visited[1:]:
        print(i)
    

bfs(R, cnt)