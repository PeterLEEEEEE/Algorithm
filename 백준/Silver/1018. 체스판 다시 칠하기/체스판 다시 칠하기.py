import sys


input = sys.stdin.readline


def solution(board):

  num_list = []

  for a in range(N-7):
    for b in range(M-7):
      w_cnt, b_cnt = 0, 0
      w_y, b_y = 0, 0

      for y in range(a, a+8):
        w_x, b_x = 0, 0
        for x in range(b, b+8):
          if board[y][x] != ans_white[w_y][w_x]:
            w_cnt += 1

          if board[y][x] != ans_black[b_y][b_x]:
            b_cnt += 1
          
          w_x += 1
          b_x += 1
        w_y += 1
        b_y += 1
      num_list.extend([w_cnt, b_cnt])

  return min(num_list)

if __name__ == '__main__':
  # write input
  N, M = map(int, input().split())
  board = [list(map(str, input().rstrip())) for _ in range(N)]
  white_row = ['W', 'B'] * 4
  black_row = ['B', 'W'] * 4

  ans_white = []
  ans_black = []
  for i in range(8):
    if i % 2 == 0:
      ans_white.append(white_row)
      ans_black.append(black_row)
    else:
      ans_white.append(black_row)
      ans_black.append(white_row)

  print(solution(board))