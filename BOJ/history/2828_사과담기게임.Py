import sys

input = sys.stdin.readline

N, M = map(int, input().split())
J = int(input())

left = 1
right = M
ans = 0

for _ in range(J):
  target = int(input())

  if left <= target and right >= target:
    continue
  elif left > target:
    ans += (left - target)
    right -= (left - target)
    left = target
  else:
    ans += (target-right)
    left += (target-right)
    right = target

print(ans)