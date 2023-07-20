import sys

input = sys.stdin.readline


vowel = ['a', 'e', 'i', 'o', 'u']

while True:
  word = input().rstrip()
  if word == 'end':
    break
  pw = list(word)
  vowel_counter = 0
  vowel_flag = 0
  consonant_counter = 0
  error_flag = 0

  for idx, alpha in enumerate(pw):
    if idx > 0:
      if pw[idx] == pw[idx-1]:
        if pw[idx] != 'e' and pw[idx] != 'o':
          error_flag = 1
          break
    if pw[idx] in vowel:
      vowel_flag = 1
      vowel_counter += 1
      consonant_counter = 0
      if vowel_counter == 3:
        error_flag = 1
        break
    else:
      vowel_counter = 0
      consonant_counter += 1
      if consonant_counter == 3:
        error_flag = 1
        break

  if error_flag == 1 or vowel_flag == 0:
    print(f"<{word}> is not acceptable.")
  else:
    print(f"<{word}> is acceptable.")