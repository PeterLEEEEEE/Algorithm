import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())


def bfs(node):
    queue = deque([node])
    visited = [0] * (n+1)
    visited[node] = 1

    while queue:
        temp = queue.popleft()

        for i in graph[temp]:
            if not visited[i]:
                queue.append(i)
                visited[i] = visited[temp] + 1
    
    return sum(visited)           

graph = [[] for _ in range(n+1)]
ans = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


for i in range(1, n+1):
    ans.append(bfs(i))

# print(ans)
print(ans.index(min(ans))+1)

