import sys

input = sys.stdin.readline

N, L = map(int, input().split())

heights = list(map(int,input().split()))
heights.sort()
for height in heights:
  if L >= height:
    L += 1

print(L)
