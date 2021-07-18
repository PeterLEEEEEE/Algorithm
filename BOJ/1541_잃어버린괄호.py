exp = input().split('-')

tmp = 0

for i in range(1, len(exp)):
    tmp += sum(map(int, exp[i].split('+')))

first = sum(map(int, exp[0].split('+')))

print(first - tmp)
