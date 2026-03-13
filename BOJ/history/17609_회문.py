import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
  word = input().rstrip()
  start = 0
  end = len(word) - 1
  flag = 0
  if word == word[::-1]:
    flag = 2
    print(0)
  else:
    while start < end:
      if word[start] == word[end]:
        start += 1
        end -= 1
      else:
        new_word_1 = word[:start] + word[start+1:]
        new_word_2 = word[:end] + word[end+1:]
        if new_word_1 == new_word_1[::-1] or new_word_2 == new_word_2[::-1]:
          print(1)
          flag = 1
          break
        else:
          print(2)
          break

