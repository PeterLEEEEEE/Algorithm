import sys


input = sys.stdin.readline


def solution(num):
  # pick 1, 2 or 3

  if num == 0:
    ans += 1
    return
  elif num < 0:
    return

  solution(num-3)
  solution(num-2)
  solution(num-1)



if __name__ == '__main__':
  # write input
  n = int(input())
  
  for _ in range(n):
    ans = 0
    solution(int(input()))
    print(ans)