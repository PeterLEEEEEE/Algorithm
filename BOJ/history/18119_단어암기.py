import sys
from collections import defaultdict

input = sys.stdin.readline
N, M = map(int, input().split())

words = []
query = defaultdict()
for _ in range(N):
    words.append(input().rstrip())

for _ in range(M):
    query.append(list(input().split()))


