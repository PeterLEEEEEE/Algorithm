
n = int(input())

pattern = input().split('*')
l_pat = len(pattern[0])
r_pat = len(pattern[1])

for _ in range(n):
    temp = input()
    
    if temp[:l_pat] == pattern[0] and temp[-r_pat:] == pattern[1] and len(''.join(pattern)) <= len(temp):
        print('DA')
    else:
        print('NE')
    