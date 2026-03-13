

while True:
    sentence = input()
    
    if sentence == '.':
        break
    
    stack = []

    for al in sentence:
        if al == '(' or al == '[':
            stack.append(al)
        
        elif al == ')':
            try:
                part = stack.pop()
            except IndexError:
                print('no')
                break
            if part != '(':
                print('no')
                break
        elif al == ']':
            try:
                part = stack.pop()
            except IndexError:
                print('no')
                break
            if part != '[':
                print('no')
                break
            
    else:
        if len(stack) == 0:
            print('yes')
        else:
            print('no')