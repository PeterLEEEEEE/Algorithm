n = int(input())
arr = []
for _ in range(n):
    arr.append(input())

patt = list(arr[0])

for j in range(n):
    for i in range(len(arr[0])):
        if arr[j][i] != patt[i]:
            patt[i] = '?'

print(''.join(patt))
