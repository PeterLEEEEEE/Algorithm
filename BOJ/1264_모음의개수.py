arr = ['a','A', 'e', 'E','u', 'U', 'i', 'I', 'o', 'O']

while True:
    cnt = 0
    n = input()

    if n == '#':
        break
    
    for i in n:
        if i in arr:
            cnt += 1
    
    print(cnt)