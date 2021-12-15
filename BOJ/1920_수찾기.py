import sys
input = sys.stdin.readline

N = int(input())
n_arr = list(map(int, input().split()))
M = int(input())
m_arr = list(map(int, input().split()))

for i in m_arr:
    if i in n_arr:
        print(1)
    else:
        print(0)