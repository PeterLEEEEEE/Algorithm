import string
n = input()
alpha = string.ascii_lowercase
alpha = list(alpha)

checker = [0] * 26
for i in n:
    if i in alpha:
        checker[alpha.index(i)] += 1

for i in checker:
    print(i, end=' ')
