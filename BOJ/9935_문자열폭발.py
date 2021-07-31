# 도저히 시간 초과 해결이 안되서 힌트봄

import sys

n = list(sys.stdin.readline().rstrip())
bomb = list(sys.stdin.readline().rstrip())

stack = []
blen = len(bomb)
for i in n:
    stack.append(i)
    if i in bomb:
        if stack[-blen:] == bomb:
            for i in range(blen):
                stack.pop()
if stack:
    print(''.join(stack))
else:
    print('FRULA')














# 시간초과 풀이
# blen = len(bomb)

# while True:
    
#     for i in range(len(n)-blen + 1):
#         if bomb == n[i:i+blen]:
#             del n[i:i+blen]
#             break
#     else:
#         if len(n):
#             print(''.join(n))
#         else:
#             print('FRULA')
#         break
    