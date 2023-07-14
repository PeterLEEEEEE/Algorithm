import sys

input = sys.stdin.readline

T = int(input())
ans = []
for _ in range(T):
  N = int(input())
  arr = []
  count = 1
  for _ in range(N):
    arr.append(list(map(int, input().split())))

  arr.sort()
  max_score = arr[0][1]
  for i in range(1, len(arr)):
    if arr[i][1] < max_score:
      count += 1
      max_score = arr[i][1]

  
  ans.append(count)

for i in ans:
  print(i)


