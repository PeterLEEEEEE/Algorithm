import sys


input = sys.stdin.readline


def solution(wall_paper):
  sharp_arrX, sharp_arrY = [], []

  for y in range(len(wall_paper)):
    for x in range(len(wall_paper[0])):
      if wall_paper[y][x] == '#':
        sharp_arrY.append(y)
        sharp_arrX.append(x)

  sharp_arrY.sort()
  sharp_arrX.sort()

  pointS = [sharp_arrY[0], sharp_arrX[0]]
  pointE = [sharp_arrY[-1]+1, sharp_arrX[-1]+1]

  return pointS + pointE

  

if __name__ == '__main__':
  # write input
  wall_paper = [".#...", "..#..", "...#."]

  print(solution(wall_paper))
