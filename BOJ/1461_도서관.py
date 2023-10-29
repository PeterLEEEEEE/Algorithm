# 틀림

import sys


input = sys.stdin.readline

def negCalc(temp_neg, negatives, flag):
  ans = 0

  temp_neg += M
  if temp_neg >= len(negatives):
    temp_neg = len(negatives) - 1
  for i in range(temp_neg, len(negatives), M):

    if i == len(negatives) - 1:
      if flag == 1:
        ans += negatives[i]
      else:
        ans += (negatives[i] * 2)
    else:
      ans += (negatives[i] * 2)

  return ans

def posCalc(temp_pos, positives, flag):
  ans = 0

  temp_pos += M
  if temp_pos >= len(positives):
    temp_pos = len(positives) - 1
  for i in range(temp_pos, len(positives), M):

    if i == len(positives) - 1:
      if flag == 1:
        ans += positives[i]
      else:
        ans += (positives[i] * 2)
    else:
      ans += (positives[i] * 2)


  return ans

def solution(arr):
  ans = 0
  negatives = [0]
  positives = [0]

  for num in arr:
    if num < 0:
      negatives.append(abs(num))
    else:
      positives.append(num)

  negatives.sort()
  positives.sort()

  temp_neg = len(negatives) % M - 1
  temp_pos = len(positives) % M - 1


  if negatives[-1] > positives[-1]:
    ans += posCalc(temp_pos, positives, 0)
    ans += negCalc(temp_neg, negatives, 1)
  else:
    ans += negCalc(temp_neg, negatives, 0)
    ans += posCalc(temp_pos, positives, 1)

  return ans

if __name__ == '__main__':
  N, M = map(int, input().split())
  arr = list(map(int, input().split()))

  print(solution(arr))
