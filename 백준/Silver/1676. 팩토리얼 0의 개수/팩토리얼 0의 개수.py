import sys


input = sys.stdin.readline


def solution(N):
  num = 1
  for i in range(N):
    num *= (i+1)

  ans = 0
  # print(list(str(num)))
  for i in list(str(num))[::-1]:
    if i == '0':
      ans += 1
    else:
      break
  print(ans)

if __name__ == '__main__':
  # write input
  N = int(input())

  solution(N)