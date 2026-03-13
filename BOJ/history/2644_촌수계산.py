from collections import deque


def bfs(start):
    queue = deque([start])
    visited[start] = 1

    while queue:
        temp = queue.popleft()

        for i in node[temp]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1
                ans[i] = ans[temp] + 1


n = int(input())
start, end = map(int, input().split())
m = int(input())

node = [[] for _ in range(n+1)]
visited = [False] * (n+1)
ans = [0] * (n+1)


for _ in range(m):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)

bfs(start)

if ans[end]:
    print(ans[end])
else:
    print(-1)