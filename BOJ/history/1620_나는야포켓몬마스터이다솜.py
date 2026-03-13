from collections import defaultdict
import sys

input = sys.stdin.readline

dic = defaultdict(str)
N, M = map(int, input().split())
str_list = [input().rstrip() for _ in range(N)]
target = [input().rstrip() for _ in range(M)]

for idx, val in enumerate(str_list, start=1):
    dic[val] = idx
    

# dic = dict(dic)
# print(dic)
for i in range(M):
    if target[i].isdigit():
        print(str_list[int(target[i])-1])
    else:
        print(dic[target[i]])