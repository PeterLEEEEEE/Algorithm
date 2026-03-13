import sys
import math 

input = sys.stdin.readline
N, M, B = map(int, input().split())

field = []
ans = math.inf
for _ in range(N):
    field.append(list(map(int, input().split())))


for i in range(257):
    max_val = 0
    min_val = 0

    for y in range(N):
        for x in range(M):
            if field[y][x] < i:
                min_val += (i - field[y][x])
            else:
                max_val += (field[y][x] - i)
    bag = max_val + B
    
    if bag < min_val:
        continue
    time = (2 * max_val) + min_val
    if time <= ans:
        ans = time
        height = i

print(ans, height)

