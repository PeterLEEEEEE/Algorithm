from re import L
import sys

input = sys.stdin.readline

N, H = map(int, input().split())

top = [0] * (H + 1)
bottom = [0] * (H + 1)

for i in range(N):
    if i % 2 == 0:
        bottom[int(input())] += 1
    else:
        top[int(input())] += 1

print(up, down)