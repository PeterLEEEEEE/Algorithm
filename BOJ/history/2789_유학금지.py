import sys
target = list(sys.stdin.readline().rstrip())

FILTER = 'CAMBRIDGE'
arr = []
for al in target:
    if al not in FILTER:
        arr.append(al)

print(''.join(arr))