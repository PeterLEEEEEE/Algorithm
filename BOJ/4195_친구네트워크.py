import sys

input = sys.stdin.readline
n = int(input())

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        parent[b] = a
        friend_cnt[a] += friend_cnt[b]
    
    print(friend_cnt[a])

for _ in range(n):
    m = int(input())
    parent = {}
    friend_cnt = {}
    for _ in range(m):
        a, b = map(str, input().split())
        if a not in parent:
            parent[a] = a
            friend_cnt[a] = 1
        if b not in parent:
            parent[b] = b
            friend_cnt[b] = 1

        union(a, b)
