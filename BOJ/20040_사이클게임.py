import sys

input = sys.stdin.readline

n, m = map(int, input().split())

parent = {}

for i in range(n):
    parent[i] = i

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a

for i in range(m):
    a, b = map(int, input().split())
    if find(a) == find(b):
        print(i+1)
        exit()
    union(a, b)

print(0)