# 맞는 것 같은데 무슨 반례가 있는지 잘 모르겠다

n = int(input())

arr = []

for _ in range(n):
    arr.append(input())


hz, vt = 0, 0
for i in range(len(arr)):
    tmp = arr[i].split('X')
    tmp.sort(key=len)
    if len(tmp[-1]) >= 2:
        hz += 1


vt_arr = [[0] * len(arr) for _ in range(len(arr))]

for i in range(len(arr)):
    for j in range(len(arr)):
        vt_arr[j][len(arr)-i-1] = arr[i][j]

for i in range(len(vt_arr)):
    tmp = ''.join(vt_arr[i]).split('X')
    tmp.sort(key=len)
    if len(tmp[-1]) >= 2:
        vt += 1

print(hz, vt)
