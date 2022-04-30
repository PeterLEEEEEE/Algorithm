import sys

input = sys.stdin.readline

N = int(input())

graph = [[0, 0] for _ in range(1001)]

start = 0
end = 0
for i in range(N):
    L, H = map(int, input().split())
    graph[L] = [L, H]
    start = min(start, L)
    end = max(end, L)



max_info = max(graph, key=lambda x:x[1])
max_idx = max_info[0]
max_val = max_info[1]


# mid = max_info[0]
ans = 0



get_area = 0
for i in range(start, max_info[0]):
    
    get_area = max(get_area, graph[i][1])
    ans += get_area

# print(ans)
get_area = 0
for i in range(end, max_info[0], -1):
    get_area = max(get_area, graph[i][1])
    ans += get_area

print(ans + max_info[1])