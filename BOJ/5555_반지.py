import sys

input = sys.stdin.readline

word = input().rstrip()
N = int(input())
word_list = [input().rstrip() for _ in range(N)]
ans = 0
for target in word_list:
  temp = ''
  for i in range(len(target)):
    end = i + len(word)

    if end > len(target):
      temp = target[i:] + target[:len(word) - len(target[i:])]
    else:
      temp = target[i:i+len(word)]

    if word == temp:
      ans += 1
      break

print(ans)