a, b = input().split()
mincnt = 50

for i in range(len(b) - len(a) + 1):
    cnt = 0
    for j in range(len(a)):
        if a[j] != b[j+i]:
            cnt += 1
    
    mincnt = min(mincnt, cnt)
    
print(mincnt)