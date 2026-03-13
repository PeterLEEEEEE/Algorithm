n = input()

if len(n) < 10:
    print(n)
else:
    for i in range(0, len(n), 10):
        print(n[i:i+10])
