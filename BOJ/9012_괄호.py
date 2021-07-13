n = int(input())
vps = []
checker = []

for _ in range(n):
    vps.append(input())

for v in vps:
    if v.count('(') != v.count(')'):
        print('NO')
    else:
        v = list(v)
        for i in v:
            if i == '(':
                checker.append(i)
            else:
                if not checker:
                    print('NO')
                    break
                checker.pop()
        else:
            print('YES')
