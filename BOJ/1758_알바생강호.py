import sys

input = sys.stdin.readline


def getTip(place, tip):
  total = tip - (place - 1)
  if total < 0:
    return 0
  return total

if __name__ == "__main__":
  N = int(input())
  ans = 0
  tips = []
  for _ in range(N):
    tips.append(int(input()))

  tips.sort(reverse=True)
  for i in range(1, N+1):
    place = i


    ans += getTip(place, tips[i-1])

  print(ans)