import sys
input = sys.stdin.readline

# 5 8 20 => 14
i = 1
while True:
  result = 0
  L, P, V = map(int, input().split())
  if L == 0 and P == 0 and V == 0: break
  if L >= (V % P):
    result = (V // P) * L + (V % P)
  else:
    result = (V // P) * L + L

  print(f"Case {i}: {result}")
  i += 1