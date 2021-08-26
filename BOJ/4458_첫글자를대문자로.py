import sys
n = int(input())
arr = []

for _ in range(n):
    arr.append(input())



for i in range(len(arr)):
    arr[i]= list(arr[i])
    arr[i][0] = arr[i][0].upper()
    print(''.join(arr[i]))



