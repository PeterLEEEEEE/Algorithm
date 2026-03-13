n = int(input())

dic = {}

for _ in range(n):
    arr = input().split('.')
    dic[arr[1]] = dic.get(arr[1], 0) + 1


temp = sorted(dic.items())

for i in temp:
    print(i[0], i[1])