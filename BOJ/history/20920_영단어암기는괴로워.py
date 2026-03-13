import sys

input = sys.stdin.readline

N, M = map(int, input().split())

words = {}
ans = []
for _ in range(N):
  word = input().rstrip()

  if len(word) >= M:
    words[word] = words.get(word, 0) + 1

words_tuple = []
for k, v in words.items():
  words_tuple.append((k, v,  len(k)))

first_order = sorted(words_tuple, key=lambda x: (-x[1], -x[2], x[0]))

for word in first_order:
  print(word[0])

