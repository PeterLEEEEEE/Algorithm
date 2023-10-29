import sys

input = sys.stdin.readline

N, K = map(int, input().split())
visited = [False] * (N+1)


flag = 0
cnt = 0
ans = 0

for i in range(2, N+1):
  if flag == 1:
    break
  for j in range(i, N+1, i):

    if visited[j] == False:
      cnt += 1
      visited[j] = True

    if cnt == K:
      ans = j
      flag = 1
      break

print(ans)