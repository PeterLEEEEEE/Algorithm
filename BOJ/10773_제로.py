n = int(input())

arr = [0]

for _ in range(n):
    num = int(input())
    if num == 0:
        arr.pop()
    else:
        arr.append(num)

print(sum(arr))
