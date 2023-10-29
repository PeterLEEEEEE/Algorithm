import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr_six = []
arr_one = []
for _ in range(M):
  a, b = map(int, input().split())
  arr_six.append(a)
  arr_one.append(b)

arr_six.sort()
arr_one.sort()

best_price_six = arr_six[0]
best_price_one = arr_one[0]
min_price = 0

while N > 0:

  if N < 6:
    if best_price_one * N < best_price_six:
      min_price += (best_price_one * N)
    else:
      min_price += (best_price_six)
    break

  else:
    if best_price_six < best_price_one * 6:
      min_price += (best_price_six * (N // 6))
      N %= 6
    else:
      N -= 1
      min_price += (best_price_one)


print(min_price)