import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
M = int(input())

network = []

for _ in range(M):
    a, b, c = map(int, input().split())
    network.append([a, b, c])

network.sort(key=lambda x:x[2])

print(network)

