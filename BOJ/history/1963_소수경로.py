import sys
from collections import deque

input = sys.stdin.readline

def calcPrime():

  for i in range(2, 100):
    if prime[i] == True:

      for j in range(2*i, 10000, i):
        prime[j] = False

def bfs():
  visited = [0 for _ in range(10000)]

  queue = deque()
  queue.append([start, 0])
  visited[start] = 1

  while queue:
    cur, cnt = queue.popleft()
    strNum = str(cur)

    if cur == end:
      return cnt

    for i in range(4):
      for j in range(10):
        if i == 0 and j == 0:
          continue
        temp = int(strNum[:i] + str(j) + strNum[i+1:])
        if visited[temp] == 0 and prime[temp]:
          visited[temp] = 1
          queue.append([temp, cnt + 1])


T = int(input())

prime = [True for _ in range(10000)]

calcPrime()

for _ in range(T):
  start, end = map(int, input().split())

  ans = bfs()

  print(ans if ans != None else "Impossible")