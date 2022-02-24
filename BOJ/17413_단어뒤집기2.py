# import sys


# n = list(sys.stdin.readline().rstrip())

# stack = []
# flag = 0
# tmp = []

# for i in n:
#     if i == '<':
#         flag = 1
        
#         if stack:
#             if ' ' not in stack:
#                 a = ''.join(stack)
#                 tmp.append(a[::-1])
            
#             else:
#                 a = ''.join(stack).split()
#                 print(a)
#                 for i in a:
#                     tmp.append(i)

#             stack.clear()

#     elif i == '>':
#         flag = 0
#         tmp.append(i)
    
#     if flag == 1:
#         tmp.append(i)

#     elif i != '>':
#         stack.append(i)
        
        
# print(''.join(tmp))

from collections import deque
import sys

input = sys.stdin.readline
n = list(input().rstrip())

stack = []
flag = 0
rev = deque()
ans = []

for i in n:
    if i =='<':
        flag = 1
    
    elif i == '>':
        flag = 0
        stack.append(i)
        ans.append(''.join(stack))
        stack.clear()
    
    if flag == 1:
        stack.append(i)
        if rev:
            ans.append(''.join(rev))
            rev.clear()

    if i != '>' and flag == 0:
        if i != ' ':
            rev.appendleft(i)
        else:
            ans.append(''.join(rev) + i)
            rev.clear()
if rev:
    ans.append(''.join(rev))

print(''.join(ans))