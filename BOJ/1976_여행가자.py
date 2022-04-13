import sys

input = sys.stdin.readline

N = int(input())
M = int(input())

parent = [i for i in range(N+1)]

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
    route = list(map(int, input().split()))

    for idx, val in enumerate(route):
        if val == 1:
            union(parent, i, idx+1) # i는 기준 도시, idx+1은 i와 연결된 도시

tour_plan = list(map(int, input().split()))

ans = set([find_parent(parent, i) for i in tour_plan])

if len(ans) == 1:
    print('YES')
else:
    print("NO")
