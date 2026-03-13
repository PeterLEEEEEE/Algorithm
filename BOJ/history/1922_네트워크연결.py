import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
M = int(input())

parent = [0] * (N + 1)
edges = []
ans = 0

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    
    return parent[x]

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    

for i in range(1, N+1):
    parent[i] = i

for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append([a, b, c])

edges.sort(key=lambda x:x[2])

for edge in edges:
    a, b, cost = edge

    if find_parent(parent, a) != find_parent(parent, b):
        union(parent, a, b)
        ans += cost

print(ans)
print(parent)

