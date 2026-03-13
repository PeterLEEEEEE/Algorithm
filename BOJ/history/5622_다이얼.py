word = input()

cnt = 0

for al in word:
    if al in 'WXYZ':
        cnt += 10
    elif al in 'TUV':
        cnt += 9
    elif al in 'PQRS':
        cnt += 8
    elif al in 'MNO':
        cnt += 7
    elif al in 'JKL':
        cnt += 6
    elif al in 'GHI':
        cnt += 5
    elif al in 'DEF':
        cnt += 4
    elif al in 'ABC':
        cnt += 3

print(cnt)