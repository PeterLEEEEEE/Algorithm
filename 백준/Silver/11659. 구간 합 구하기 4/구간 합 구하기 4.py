import sys


input = sys.stdin.readline


def solution():
  sumArr = [0] * (N + 1)
  sumArr[0] = 0
  for i in range(1, N+1):
    sumArr[i] = sumArr[i-1] + arr[i-1]

  return sumArr

if __name__ == '__main__':
  # write input
  N, M = map(int, input().split())
  arr = list(map(int, input().split()))

  sumArr = solution()
  
  for _ in range(M):
    start, end = map(int, input().split())
    print(sumArr[end] - sumArr[start-1])
