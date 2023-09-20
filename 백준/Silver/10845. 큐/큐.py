import sys
from collections import deque

input = sys.stdin.readline


def solution(commands):

  queue = deque()

  for command in commands:
    if command.startswith('push'):

      queue.append(int(command.split()[1]))

    elif command == "pop":
      if len(queue) > 0:
        print(queue.popleft())
      else:
        print(-1)
    elif command == "size":
      print(len(queue))
    elif command == "empty":
      if len(queue) == 0:
        print(1)
      else:
        print(0)
    elif command == "front":
      if len(queue) == 0:
        print(-1)
      else:
        print(queue[0])
    elif command == "back":
      if len(queue) == 0:
        print(-1)
      else:
        print(queue[-1])
    
if __name__ == '__main__':
  # write input
  N = int(input())

  commands = [input().rstrip() for _ in range(N)]

  solution(commands)