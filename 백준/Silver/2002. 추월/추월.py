import sys

input = sys.stdin.readline

N = int(input())

in_arr = [input().rstrip() for _ in range(N)]
out_arr = [input().rstrip() for _ in range(N)]

in_dic = {}
ans = 0

for i in range(len(in_arr)):
  in_dic[in_arr[i]] = i


for i in range(N-1):
  for j in range(i+1, N):
    if in_dic[out_arr[i]] > in_dic[out_arr[j]]:
      ans+=1
      break


print(ans)