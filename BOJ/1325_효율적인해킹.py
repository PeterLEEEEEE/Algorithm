import sys
from collections import deque

input = sys.stdin.readline


N, M = map(int, input().split())
graph = []
graph = [[] for _ in range(N+1)]


def bfs(v, N):
    q = deque([v])
    cnt = 0
    visited = [False] * (N+1)
    visited[v] = True
    while q:
        temp = q.popleft()
        cnt += 1
        for i in graph[temp]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
    return cnt
for i in range(M):
    a, b = map(int, input().split())
    
    graph[b].append(a)

ans = []
max_cnt = 0
idx = 0
for i in range(1,N+1):
    if graph[i]:
        temp_cnt = bfs(i, N)
        if max_cnt < temp_cnt:
            ans = []
            max_cnt = temp_cnt
            idx = i
            ans.append(idx)
        elif max_cnt == temp_cnt:
            idx = i
            ans.append(idx)
        
print(*ans)
