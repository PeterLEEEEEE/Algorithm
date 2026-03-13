n = int(input())

stack = []
cnt = 0

for _ in range(n):
    arr = list(input())

    for i in arr:
        if not stack or stack[-1] != i:
            stack.append(i)
        elif stack[-1] == i:
            stack.pop()

    if not stack:
        cnt += 1

    stack.clear()

print(cnt)
