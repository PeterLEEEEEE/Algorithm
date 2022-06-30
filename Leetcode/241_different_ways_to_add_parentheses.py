exp = '2*3-4*5'

def calc(left, right, e):
    temp = []
    for l in left:
        for r in right:
            temp.append(eval(str(l) + e + str(r)))
    
    return temp

def sol(exp):
    ans = []
    if exp.isdigit():
        return [int(exp)]

    for i, v in enumerate(exp):
        if v in '-+*':
            left = sol(exp[:i])
            right = sol(exp[i+1:])
            

            ans.extend(calc(left, right, v))

    return ans


print(sol(exp))