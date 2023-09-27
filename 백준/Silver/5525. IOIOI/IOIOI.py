import sys

n = int(input())
m = int(input())

input = sys.stdin.readline

arr = input()

ans = 0
a = 'IOI'
b = 'OI'

if n == 1:
    pat = a
elif n >= 2:
    pat = a + (b * (n - 1))

for i in range(len(arr) - len(pat)):
    if arr[i:i+len(pat)] == pat:
        ans += 1

print(ans)