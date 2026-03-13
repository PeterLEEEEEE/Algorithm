import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = list(map(int, input().split()))

for i in range(m):
  arr.sort()
  added = arr[0]+arr[1]

  arr[0], arr[1] = added, added
  if i == m-1:
    break

  # print(arr)
print(sum(arr))