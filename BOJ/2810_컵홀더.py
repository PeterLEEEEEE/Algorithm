n = int(input())

sentence = input()

i = 0
cnt = 0
while i < len(sentence):
    if sentence[i:i+2] == 'LL':
        cnt += 1
        i += 2
    else:
        cnt += 1
        i += 1

if 'LL' in sentence:
    cnt += 1

print(cnt)