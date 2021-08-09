import itertools
n = int(input())

def factorial(num):
    if num == 1:
        return 1
    else:
        result = 1
        for i in range(2, num+1):
            result *= i
    
    return result


for _ in range(n):
    w, e = map(int, input().split())
    west = [0] * w
    east = [0] * e
    
    ans = factorial(e) // (factorial((e-w)) * factorial(w))

    print(ans)
    

