import sys
from collections import deque

input = sys.stdin.readline

S, E, Q = input().split()

dic = {}
while True:
  try:
    t, name = input().split()
    dic[name] = dic.get(name, []) + [t]
  except:
    break

ans = 0
for k, v in dic.items():
  start_flag = 0
  end_flag = 0

  if len(v) > 1:

    if v[0] <= S:
      start_flag = 1

    for i in range(1, len(dic[k])):
      if E <= dic[k][i] <= Q:
        end_flag = 1


    if start_flag == 1 and end_flag == 1:
      ans += 1


print(ans)