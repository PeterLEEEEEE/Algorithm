n = input()

cnt = 0
stack = []

for i in range(len(n)):
    if not stack:
        cnt += 10
    elif stack[-1] == n[i]:
        cnt += 5
    else:
        cnt += 10

    stack.append(n[i])

print(cnt)