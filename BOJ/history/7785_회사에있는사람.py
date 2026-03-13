import sys
n = int(input())

dic = {}

for _ in range(n):
    arr = list(input().split())

    dic[arr[0]] = arr[1]
    
ans = []
for i in dic.keys():
    if dic[i] == 'enter':
        ans.append(i)

ans.sort(reverse = True)
for i in ans:
    print(i)