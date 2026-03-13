import sys

input = sys.stdin.readline

# word = input().rstrip()
# min_alpha = min(word)

# arr = []
# flag_idx = 0

# for idx, alpha in enumerate(word[:-2]):
#   if alpha == min_alpha:
#     temp = word[:idx+1]
#     flag_idx = idx
#     arr.append(word[:idx+1][::-1])
#     break

# min_alpha = min(word[flag_idx+1:-1])

# for idx, alpha in enumerate(word[flag_idx+1:-1]):
#   if alpha == min_alpha:
#     temp = word[flag_idx+1:idx+flag_idx+2]
#     flag_idx = idx+flag_idx+1
#     arr.append(temp[::-1])
#     break

# if word[flag_idx+1:] > word[flag_idx+1:][::-1]:
#   arr.append(word[flag_idx+1:][::-1])
# else:
#   arr.append(word[flag_idx+1:])

# print(''.join(arr))
string = input().rstrip()

answer = "z" * len(string)

for i in range(1, len(string) - 1):
    for j in range(i + 1, len(string)):
        s1 = string[:i][::-1]
        s2 = string[i:j][::-1]
        s3 = string[j:][::-1]
        new_string = s1 + s2 + s3
        answer = min(answer, new_string)

print(answer)