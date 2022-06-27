import sys

sys.setrecursionlimit(100000000)
input = sys.stdin.readline
n, m = map(int, input().split())


parent = {}
for i in range(n+1):
    parent[i] = i

def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]

def union(a, b):
    a = find(a)
    b = find(b)
    
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

for i in range(m):
    z, x, y = map(int, input().split())
    if z == 0:
        union(x, y)
    elif z == 1:
        if find(x) == find(y):
            print('YES')
        else:
            print('NO')


