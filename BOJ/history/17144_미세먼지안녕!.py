import sys

input = sys.stdin.readline

R, C, T = map(int, input().split())
field = []

for _ in range(R):
    field.append(list(map(int, input().split())))

