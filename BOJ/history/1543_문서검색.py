import sys
n = sys.stdin.readline().rstrip()
target = sys.stdin.readline().rstrip()

t_len = len(target)

i = 0
cnt = 0
while i < len(n):
    
    if target == n[i:i+t_len]:
        cnt += 1
        i += t_len
    else:
        i += 1

print(cnt)