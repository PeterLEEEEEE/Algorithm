'''


'''

word = input()
cap_word = word.upper()

set_word = list(set(cap_word))

tmp = []

for al in set_word:
    tmp.append(cap_word.count(al))

maxnum = max(tmp)

if tmp.count(maxnum) != 1:
    print('?')
else:
    print(set_word[tmp.index(maxnum)])
