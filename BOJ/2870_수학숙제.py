import sys

input = sys.stdin.readline

N = int(input())

arr = [input().rstrip() for _ in range(N)]
num_arr = []
for l in arr:
  num = ''
  temp = list(l)
  for i in temp:
    if i.isdigit():
      num += i
    else:
      if num:
        num_arr.append(int(num))
      num = ''
  if num:
    num_arr.append(int(num))
num_arr.sort()

for i in num_arr:
  print(i)