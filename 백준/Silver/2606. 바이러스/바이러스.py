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

for i in range(1, 101):
    network[i] = []

for i in arr:
    # network[i[0]] = network.get(i[0], []) + [i[1]]
    network[i[0]].append(i[1])
    network[i[1]].append(i[0])
    # network[i[1]] = network.get(i[1], []) + [i[0]]


if len(network[1]) == 0:
    print(0)
else:
    dfs(network, 1)
    print(len(visited)-1)

