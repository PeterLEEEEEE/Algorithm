import sys


input = sys.stdin.readline


def solution(lev):
  if lev == k:
    ans.add(''.join(selected))
    return

  for i in range(n):
    if visited[i]:
      continue

    selected.append(cards[i])
    visited[i] = True

    solution(lev+1)

    selected.pop()
    visited[i] = False


if __name__ == '__main__':
  # write input
  n = int(input())
  k = int(input())
  ans = set()
  selected = []
  visited = [False] * n
  cards = [input().rstrip() for _ in range(n)]

  solution(0)

  print(len(ans))