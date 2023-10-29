import sys


input = sys.stdin.readline
S = int(input())
cnt = 0
i = 1
if S == 1:
    cnt = 1
else:
    while True:
        if S > i:
            S -= i
            cnt += 1
        elif S == i:
            cnt += 1
            break
        else:
            break
        i += 1

print(cnt)