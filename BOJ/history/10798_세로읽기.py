arr = []

for _ in range(5):
    arr.append(input())

arr2 = []
idx = 0

for i in range(len(arr)):
    if idx < len(arr[i]):
        idx = len(arr[i])

# idx = [max(len(i)) for i in arr]


for i in range(idx):
    for j in range(5):
        try:
            arr2.append(arr[j][i])
        except IndexError:
            pass

print(''.join(arr2))
