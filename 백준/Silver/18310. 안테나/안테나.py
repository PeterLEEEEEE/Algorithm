import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
dic = {}
mid = 0
if len(arr) % 2 == 0:
  mid = len(arr) // 2 - 1
elif len(arr) % 2 == 1:
  mid = len(arr) // 2

# for house in arr:
#   dic[house] = 0
#   for i in arr:
#     dic[house] += abs(house - i)

print(arr[mid])