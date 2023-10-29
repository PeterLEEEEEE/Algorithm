import sys
from collections import defaultdict

input = sys.stdin.readline
S = input().strip()
s_list = list(S)
dic = defaultdict(int)
temp = s_list[0]
dic[temp] = 1
for i in range(1, len(s_list)):

    if temp != s_list[i]:
        temp = s_list[i]
        dic[s_list[i]] += 1


if len(dic.values()) == 1:
    print(0)
else:
    print(min(dic.values()))