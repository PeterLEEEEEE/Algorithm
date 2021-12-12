def dfs(network, first):
    for i in network[first]:
        if i not in visited:
            visited.append(i)
            dfs(network, i)


coms = int(input())
conn = int(input())

arr = []
visited = []
network = {}

for _ in range(conn):
    arr.append(list(map(int, input().split())))

for i in arr:
    network[i[0]] = []
    network[i[1]] = []

for i in arr:
    network[i[0]].append(i[1])
    network[i[1]].append(i[0])

dfs(network, 1)
print(len(visited)-1)
