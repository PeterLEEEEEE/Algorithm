n = int(input())


for _ in range(n):
    category = int(input())
    dic = {}
    ans = 1
    for _ in range(category):
        name = input().split()

        if name[1] in dic.keys():
            tmp = dic[name[1]]
            tmp += 1
            dic[name[1]] = tmp
        else:
            dic[name[1]] = 1

    for val in dic.values():
        ans *= (val+1)

    print(ans - 1)
