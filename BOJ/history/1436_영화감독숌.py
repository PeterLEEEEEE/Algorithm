import sys


input = sys.stdin.readline


def solution(N):
  ans = 666
  cnt = 0

  while True:

    if '666' in str(ans):
      cnt += 1

    if cnt == N:
      break

    ans += 1

  print(ans)

if __name__ == '__main__':
  # write input
  N = int(input())

  solution(N)