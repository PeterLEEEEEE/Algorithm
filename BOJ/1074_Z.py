import sys


input = sys.stdin.readline

dy = [0, 1, 0]
dx = [1, -1, 1]

def solution(ans, N, r ,c):
  ans = 0

  while N != 0:
    N -= 1
    board_size = 2 ** N

    if r < board_size and c < board_size:
      continue

    elif r < board_size and c >= board_size:
      ans += board_size * board_size
      c -= board_size

    elif r >= board_size and c < board_size:
      ans += board_size * board_size * 2
      r -= board_size

    else:
      ans += board_size * board_size * 3
      r -= board_size
      c -= board_size

  return ans


if __name__ == '__main__':
  # write input
  N, r, c = map(int, input().split())

  # board = [[0]*(board_size) for _ in range(board_size)]
  # start_idx = [1, 1]


  print(solution(0, N, r, c))

