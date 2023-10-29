import sys
from itertools import permutations

max_ans = float("-inf")
min_ans = sys.maxsize

N = int(input())

values = list(map(int, input().split()))
operators = list(map(int, input().split()))
orders = []
ops = ['+', '-', '*', '/']

for i in range(len(ops)):
  orders.extend([ops[i]] * operators[i])

def calc(temp):
  sum_val = values[0]

  for i in range(len(temp)):
    if temp[i] == '+':
      sum_val += values[i+1]
    elif temp[i] == '-':
      sum_val -= values[i+1]
    elif temp[i] == '*':
      sum_val *= values[i+1]
    elif temp[i] == '/':
      if sum_val < 0:
        sum_val *= -1
        sum_val //= values[i+1]
        sum_val *= -1
      else:
        sum_val //= values[i+1]

    # if temp == ['-', '/', '+', '+', '*']:
    #   print(sum_val)

  return sum_val


if __name__ == '__main__':
  ops = set(permutations(orders, len(orders)))

  for op in ops:
    temp = calc(list(op))
    max_ans = max(max_ans, temp)
    min_ans = min(min_ans, temp)

  print(max_ans)
  print(min_ans)