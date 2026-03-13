# https://www.acmicpc.net/problem/11403

import sys

input = sys.stdin.readline
from collections import deque

N = int(input())
graph = [[] for _ in range(N+1)]
arr = []


def bfs(start):
    q = deque()
    visited = [0] * (N+1)
    q.append(start)
    while q:
        curr = q.popleft()
        for node in graph[curr]:
            if not visited[node]:
                visited[node] = 1
                q.append(node)
    
    print(*visited[1:])


for i in range(N):
    arr = list(map(int, input().split()))

    for j in range(N):
        if arr[j]:
            graph[i+1].append(j+1)


for i in range(1, N+1):
    bfs(i)
