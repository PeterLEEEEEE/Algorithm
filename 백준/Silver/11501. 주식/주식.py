import sys

input = sys.stdin.readline

T = int(input())


for _ in range(T):
  N = int(input())
  arr = list(map(int, input().split()))
  benefit = 0
  # max_price = max(arr)
  # for day, price in enumerate(arr):

  #   if price != max_price:
  #     benefit += (max_price - price)

  #   elif price == max_price:
  #     if day+1 <= len(arr) - 1:
  #       max_price = max(arr[day+1:])

  max_price = arr[-1]
  for i in range(N-2, -1, -1):
    if arr[i] > max_price:
      max_price = arr[i]
    else:
      benefit += (max_price - arr[i])
      
  print(benefit)
