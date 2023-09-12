import sys

input = sys.stdin.readline


def distance(arr):
  dist = []
  for i in range(len(arr)-1):
    dist.append(arr[i+1]-arr[i])

  dist.sort(reverse=True)

  return sum(dist[K-1:])

if __name__ == '__main__':
  N = int(input())
  K = int(input())
  arr = list(map(int, input().split()))

  arr.sort()

  print(distance(arr))