import sys

input = sys.stdin.readline
# N = int(input())
# M = int(input())

# positions = list(map(int, input().split()))
# answer = 0

# if M == 1:
#     print(max(positions[0], N - positions[0]))
# else:
#     answer = max(positions[0], abs(positions[-1]-N))
#     start_range = positions[0]
#     for i in range(1, len(positions)):
#         answer = max(positions[i] - start_range, answer)
#         start_range = positions[i]

#     print(answer)

N = int(input())
M = int(input())

positions = list(map(int, input().split()))
len_positions = len(positions)

min_height = 0


if len_positions == 1:
    min_height = max(positions[0] - 0, N - positions[0])

else:
    for i in range(len_positions):

        if i == 0:
            height = positions[i] - 0

        elif i == len_positions - 1:
            height = N - positions[i]

        else:
            tmp = positions[i] - positions[i-1]
            if tmp % 2:
                height = tmp // 2 + 1
            else:
                height = tmp // 2

        min_height = max(height, min_height)

print(min_height)