word = input()

jcnt,icnt = 0, 0

for i in range(len(word)-2):
    if word[i:i+3] == 'JOI':
        jcnt += 1
    elif word[i:i+3] == 'IOI':
        icnt += 1

print(jcnt)
print(icnt)