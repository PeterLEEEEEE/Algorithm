import sys

input = sys.stdin.readline

n = int(input())
dic = {}
for _ in range(n):
  name, day, month, year = input().split()

  if len(day) == 1:
    day = '0' + day
  if len(month) == 1:
    month = '0' + month

  dic[name] = int(year + month + day)

ans_arr = list(dict(sorted(dic.items(), key=lambda x: x[1])).keys())

print(ans_arr[-1])
print(ans_arr[0])
