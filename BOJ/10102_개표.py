n = int(input())

arr = list(input())

cntA, cntB = 0, 0

for i in range(n):
    if arr[i] == 'A':
        cntA += 1
    else:
        cntB += 1


if cntA > cntB:
    print('A')
elif cntA < cntB:
    print('B')
else:
    print('Tie')
