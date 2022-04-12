import sys

input = sys.stdin.readline

N = int(input())

graph = []


for _ in range(N):
    L, H = map(int, input().split())
    graph.append([L,H])
    graph.sort(key=lambda x:x[0])


print(graph)
max_info = max(graph, key=lambda x:x[1])
start = graph[0][0]
end = graph[-1][0]
mid = max_info[0]
ans = max_info[1]
max_idx = graph.index(max_info)

start_to_mid = [0] * (mid - start)
# while True:
#     if pivot < graph[0][0]:
#         break
pivot = start
for i in range(len(start_to_mid)):
    ans += pivot
    