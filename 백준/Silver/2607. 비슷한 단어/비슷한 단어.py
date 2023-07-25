import sys

input = sys.stdin.readline

N = int(input())

ans = 0
target_word = list(input().rstrip())
for _ in range(N-1):
  word = input().rstrip()

  temp = target_word[:]
  false_cnt = 0

  for alpha in word:
    if alpha in temp:
      temp.remove(alpha)
    else:
      false_cnt += 1
  if false_cnt < 2 and len(temp) < 2:
    ans += 1

print(ans)