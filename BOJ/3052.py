remainder = []

for _ in range(10):
    n = int(input())
    if (n % 42) not in remainder:
        remainder.append(n % 42)


print(len(remainder))
