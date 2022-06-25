# 0 = 양
# 1 = 늑대
from collections import deque


def bfs(graph, lamb, wolf):
    q = deque([[0, lamb, wolf, set()]])
    
    max_cnt = 0
    
    while q:
        cur_node, lamb_cnt, wolf_cnt, avail_nodes = q.popleft()
        max_cnt = max(max_cnt, lamb_cnt)
        avail_nodes.update(graph[cur_node])
        
        for i in avail_nodes:
            if info[i] == 0:
                q.append([i, lamb_cnt+1, wolf_cnt, avail_nodes - {i}])
            
            else:
                if lamb_cnt - 1 == wolf_cnt:
                    continue
                else: 
                    q.append([i, lamb_cnt, wolf_cnt+1, avail_nodes - {i}])
            
            # print(lamb_cnt, wolf_cnt)
            
            
    return max_cnt    
                    
def solution(info, edges):
    answer = 0
    graph = [[] for _ in range(len(info))]
    lamb_cnt = 1
    wolf_cnt = 0
    for edge in edges:
        graph[edge[0]].append(edge[1])
        # graph[edge[1]].append(edge[0])
    # print(graph)
    answer = bfs(graph, lamb_cnt, wolf_cnt)
    return answer


info = [0,0,1,1,1,0,1,0,1,0,1,1]
edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]

print(solution(info, edges))