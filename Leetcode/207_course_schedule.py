from collections import defaultdict
numCourses = 2
prerequisites = [[1,0],[0,1]]

graph = defaultdict(list)
his = set()
visited = set()


for a, b in prerequisites:
    graph[a].append(b)

def dfs(x):
    if x in his:
        return False

    if x in visited:
        return True

    his.add(x)
    
    for i in graph[x]:
        if not dfs(i):
            return False
    
    his.remove(x)
    visited.add(x)

    return True

for i in list(graph):
    if dfs(i) == False:
        print(False)
        exit()


