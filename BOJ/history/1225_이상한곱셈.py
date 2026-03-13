a, b = map(str, input().split())
total = 0

a = list(a)
b = list(b)

for i in a:
    for j in b:
        total += (int(i) * int(j))

print(total)
