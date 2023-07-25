import sys

input = sys.stdin.readline

N = int(input())

target = int(input())
arr = []
ans = 0
for _ in range(N-1):
  arr.append(int(input()))
if N == 1:
  print(0)
else:

  while True:
    arr.sort(reverse=True)
    if target <= arr[0]:
      target += 1
      arr[0] -= 1
      ans += 1
    else:
      break

  print(ans)
