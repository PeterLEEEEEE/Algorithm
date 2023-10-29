import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

mid = 0
if len(arr) % 2 == 0:
  mid = len(arr) // 2 - 1
elif len(arr) % 2 == 1:
  mid = len(arr) // 2

print(arr[mid])