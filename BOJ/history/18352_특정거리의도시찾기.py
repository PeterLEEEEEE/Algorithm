import sys
from collections import deque

input = sys.stdin.readline

N, M, K, X = map(int, input().split())

visited = [-1] * (N+1)
visited[X] = 0
flag = 0

arr = [[] for _ in range(N+1)]

for _ in range(M):
  a, b = map(int, input().split())
  arr[a].append(b)

def bfs(start):
  queue = deque()
  queue.append(start)

  while queue:
    temp = queue.popleft()

    for i in arr[temp]:
      if visited[i] == -1:
        visited[i] = visited[temp] + 1
        queue.append(i)

bfs(X)

for i in range(1, N+1):
  if visited[i] == K:
    print(i)
    flag = 1

if flag == 0:
  print(-1)

