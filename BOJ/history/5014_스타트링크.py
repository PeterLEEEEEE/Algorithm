import sys
from collections import deque
input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())
# F = 총 층수, S = 사람 위치, G = 회사 위치, U = 올라갈 수 있는 수, D = 내려갈 수 있는 수
flag = 0

def bfs(S):
    q = deque([S])
    visited = [0] * (F+1)
    visited[S] = 1
    
    while q:
        temp = q.popleft()
        if temp == G:
            return visited[G] - 1
            
        up_status = temp + U
        down_status = temp - D
        if up_status <= F and not visited[up_status]:
            q.append(up_status)
            visited[up_status] = visited[temp] + 1
        
        if down_status > 0 and not visited[down_status]:
            q.append(down_status)
            visited[down_status] = visited[temp] + 1
    
    return -1

ans = bfs(S)
if ans == -1:
    print('use the stairs')
else:
    print(ans)