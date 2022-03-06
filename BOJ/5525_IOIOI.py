import sys

# n = int(input())
# m = int(input())

# arr = sys.stdin.readline().rstrip()

# a = 'IOI'
# b = 'OI'
# cnt = 0

# if n == 1:
#     pat = a
# elif n >= 2:
#     pat = a + (b * (n-1))


# for i in range(len(arr) - len(pat)):
#     if arr[i:i+len(pat)] == pat:
#         cnt += 1

# print(cnt)
import sys

n = int(input())
m = int(input())

input = sys.stdin.readline

arr = input().rstrip()

ans = 0
flag = 0
a = 'IOI'
b = 'OI'

if n == 1:
    pat = a
elif n >= 2:
    pat = a + (b * (n - 1))

for i in range(len(arr) - len(pat)):
    if flag == 1:
        flag = 0
        continue
    
    if arr[i:i+len(pat)] == pat:
        flag = 1
        ans += 1
        

print(ans)