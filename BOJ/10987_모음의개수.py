n = input()

vowels = ['a', 'e', 'i', 'o', 'u']

cnt = 0

for i in n:
    if i in vowels:
        cnt += 1

print(cnt)