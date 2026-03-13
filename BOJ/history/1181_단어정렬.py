import sys
input = sys.stdin.readline

N = int(input())
words = []
for _ in range(N):
  words.append(input().rstrip())

words = sorted(set(words))
words.sort(key=lambda x: len(x))

for word in words:
  print(word)