N, M = map(int, input().split())

li = [input() for _ in range(N)]
s, dis = '', 0

for j in range(M):
    d = {}
    for i in range(N):
        d[li[i][j]] = d.get(li[i][j], 0) + 1
    d_li = sorted([[k, v] for k, v in d.items()])
    d_li.sort(key=lambda x:x[0])
    d_li.sort(key=lambda x:x[1], reverse=True)
    s += d_li[0][0]
    dis += N-d_li[0][1]

print(s)
print(dis)
    