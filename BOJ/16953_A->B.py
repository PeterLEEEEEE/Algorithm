import sys


input = sys.stdin.readline
A, B = map(int, input().split())

cnt = 1
while True:
    if A == B:
        break
    elif A > B or (B % 10 != 1 and B % 2 != 0):
        cnt = -1
        break
    
    elif B % 10 == 1:
        B = B // 10
    elif B % 2 == 0:
        B = B // 2
    
    cnt += 1

print(cnt)