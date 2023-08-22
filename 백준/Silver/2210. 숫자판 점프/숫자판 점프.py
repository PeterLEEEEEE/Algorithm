import sys
from collections import deque

input = sys.stdin.readline

arr = [list(map(int, input().split())) for _ in range(5)]

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]


def dfs(y, x, moves, temp):

  if moves == 6:
    ans_set.add(temp)
    return

  for i in range(4):
    ny = dy[i] + y
    nx = dx[i] + x

    if 0 <= ny < 5 and 0 <= nx < 5 and moves <= 5:
      dfs(ny, nx, moves+1, temp+str(arr[ny][nx]))

  return

ans_set = set()
for y in range(5):
  for x in range(5):
    moves = 0
    temp = ''
    dfs(y, x, moves, temp)

print(len(ans_set))