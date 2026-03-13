from string import ascii_lowercase
import sys 
alpha = list(ascii_lowercase)
alpha_cnt = [0] * 26

n = sys.stdin.read()

for i in n:
    if i in alpha:
        alpha_cnt[alpha.index(i)] += 1

maxnum = max(alpha_cnt)

for i in range(len(alpha)):
    if alpha_cnt[i] == maxnum:
        print(alpha[i], end='')
