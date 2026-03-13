import sys

input = sys.stdin.readline

N = int(input())

arr = [input().rstrip() for _ in range(N)]

ans = 1
start_idx = len(arr[0]) - 1
end_idx = len(arr[0])
max_len = len(arr)

while start_idx > 0:
  temp = []
  for num in arr:
    temp.append(num[start_idx:end_idx])

  if len(set(temp)) == max_len:
    break
  else:
    ans += 1
  start_idx -= 1

print(ans)