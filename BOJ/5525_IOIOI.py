import sys

n = int(input())
m = int(input())

arr = sys.stdin.readline().rstrip()

a = 'IOI'
b = 'OI'
cnt = 0

if n == 1:
    pat = a
elif n >= 2:
    pat = a + (b * (n-1))


for i in range(len(arr) - len(pat)):
    if arr[i:i+len(pat)] == pat:
        cnt += 1

print(cnt)
