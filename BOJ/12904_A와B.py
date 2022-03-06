# import sys

# input = sys.stdin.readline

# s = input().rstrip()
# t = input().rstrip()

# swap_chance = len(t) - len(s)
# swap_cnt = 0
# ans = 0

# def swap(s):
#     arr = []
#     for i in s:
#         if i == 'A':
#             arr.append('B') 
#         elif i == 'B':
#             arr.append('A')
    
#     return ''.join(arr) + 'B'


# def cur(s, swap_cnt):
#     # global ans
#     if s == t:
#         print(1)
#         exit()
#     if swap_cnt == swap_chance:
#         return
    
#     cur(s + 'A', swap_cnt + 1)
#     cur(swap(s), swap_cnt + 1)
    
#     return 

# cur(s, swap_cnt)

import sys

input = sys.stdin.readline

s = list(input().rstrip())
t = list(input().rstrip())

flag = 0

while len(s) != len(t):
    if t[-1] == 'A':
        t.pop()
    elif t[-1] == 'B':
        t.pop()
        t = t[::-1]
    
    if s == t:
        flag = 1
        break
    
if flag == 1:
    print(1)
else:
    print(0)