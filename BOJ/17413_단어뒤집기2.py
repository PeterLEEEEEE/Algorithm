import sys
from collections import deque

n = list(sys.stdin.readline().rstrip())

stack = []
flag = 0
tmp = []

for i in n:
    if i == '<':
        flag = 1
        
        if stack:
            if ' ' not in stack:
                a = ''.join(stack)
                tmp.append(a[::-1])
            
            else:
                a = ''.join(stack).split()
                print(a)
                for i in a:
                    tmp.append(i)

            stack.clear()

    elif i == '>':
        flag = 0
        tmp.append(i)
    
    if flag == 1:
        tmp.append(i)

    elif i != '>':
        # if i != ' ':
        stack.append(i)
        
        
print(''.join(tmp))

