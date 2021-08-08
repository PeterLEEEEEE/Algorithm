n = input()

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
cesar = 'DEFGHIJKLMNOPQRSTUVWXYZABC'
ans = []
for i in n:
    tmp = cesar.index(i)
    ans.append(alphabet[tmp])
    
print(''.join(ans))