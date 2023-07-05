import sys
input = sys.stdin.readline

T = int(input())

c_list = []

for _ in range(T):
  c_list.append(int(input()))


for c in c_list:
  quarter, dime, nickel, penny = 0, 0, 0, 0
  while c != 0:
    if c >= 25:
      quarter = c // 25
      c %= 25
    if c >= 10:
      dime = c // 10
      c %= 10
    if c >= 5:
      nickel = c // 5
      c %= 5
    else:
      penny = c
      break
  print(quarter, dime, nickel, penny)



