from collections import defaultdict

tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]

graph = defaultdict(list)

for a,b in sorted(tickets):
    graph[a].append(b)

def dfs(node):
    stack = [node]
    ans = []
    while stack:
        while graph[stack[-1]]:
            stack.append(graph[stack[-1]].pop(0))
            print(graph, stack)
        
        ans.append(stack.pop())
        print(ans)
    return ans[::-1]

print(graph)
dfs('JFK')

