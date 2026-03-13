import sys
from itertools import combinations
# 0 빈 칸
# 1 집
# 2 치킨집

n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
homes = []
gyochon = []
ans = float('inf')
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            homes.append([i, j])
        elif board[i][j] == 2:
            gyochon.append([i, j])

for combo in list(combinations(gyochon, m)):
    min_sum = 0
    for home in homes:
        min_distance = float('inf')
        for i in range(m): # 치킨 집
            min_distance = min(min_distance, abs(home[0]-combo[i][0]) + abs(home[1]-combo[i][1]))
        
        min_sum += min_distance
    
    ans = min(ans, min_sum)

print(ans)