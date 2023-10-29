import sys
import string

input = sys.stdin.readline
alpha_dict = dict()


def solution(words):
  ans = 0

  for word in words:
    for i in range(len(word)):
      num = 10 ** (len(word) - i - 1)
      alpha_dict[word[i]] = alpha_dict.get(word[i], 0) + num
      # alpha_dict[word[i]] += num

  num_list = sorted(alpha_dict.values(), reverse=True)

  for i in range(len(num_list)):
    ans += num_list[i] * (9 - i)

  return ans


if __name__ == '__main__':
  N = int(input())
  words = []
  max_len = 0
  for _ in range(N):
    word = input().rstrip()
    words.append(word)

  print(solution(words))