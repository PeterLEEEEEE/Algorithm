import sys
input = sys.stdin.readline

N = int(input())
n_arr = list(map(int, input().split()))
M = int(input())
m_arr = list(map(int, input().split()))

# for i in m_arr:
#     if i in n_arr:
#         print(1)
#     else:
#         print(0)

n_dict = {}

for i in n_arr:
    n_dict[i] = n_dict.get(i, 0) + 1

for i in m_arr:
    n_dict[i] = n_dict.get(i, 0)

    if n_dict[i] == 0:
        print(0)
    else:
        print(1)
    