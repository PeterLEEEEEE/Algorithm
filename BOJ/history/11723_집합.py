import sys


input = sys.stdin.readline


def solution(M):
  result = set()

  for _ in range(M):
    temp = input().rstrip()

    if temp == "all":
      result = set(range(1, 21))
    elif temp == "empty":
      result = set()
    else:
      command, num = temp.split()
      num = int(num)
      if command == "add":
        result.add(num)
      elif command == "remove":
        result.discard(num)
      elif command == "check":
        if num in result:
          print(1)
        else:
          print(0)
      elif command == "toggle":
        if num in result:
          result.discard(num)
        else:
          result.add(num)

if __name__ == '__main__':
  # write input

  M = int(input())

  solution(M)

