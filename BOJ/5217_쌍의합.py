n = int(input())

for _ in range(n):
    num = int(input())

    print(f'Pairs for {num}:', end = ' ')
    i = 1

    while i < num - i:
        if i >= 2:
            print(',')
        if i != num - i:
            print(i, num - i, end = '')
            
        i += 1
        
    print()