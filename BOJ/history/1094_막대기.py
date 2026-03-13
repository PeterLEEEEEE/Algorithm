x = int(input())

stick = 64
arr = [64]
cnt = 0
while True:
    stick //= 2
    arr.append(stick)

    if stick == 1:
        break

for i in range(len(arr)):
    if x >= arr[i]:
        cnt += 1
        x -= arr[i]
    if x == 0:
        break
print(arr)
print(cnt)