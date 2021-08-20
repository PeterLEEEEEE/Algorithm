s = "([)]"

stack = []

flag = 0

for i in s:
    if i == '(' or i == '{' or i == '[':
        stack.append(i)
    
    if stack:
        tmp = stack.pop()
        if i == ')':
            if tmp != '(':
                flag = 1
                
        elif i == '}':
            if tmp != '{':
                flag = 1
                
        elif i == ']':
            if tmp != '[':
                flag = 1
                
    else:
        if i == ')' or i == ']' or i == '}':
            flag == 1
    
    if flag == 1:
        break

if flag == 1:
    return False
else:
    return True