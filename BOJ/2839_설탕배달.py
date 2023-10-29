import sys
input = sys.stdin.readline

N = int(input())
answer = 0

if N == 1 or N == 2:
    N = -1

while N > 0:
    if N % 5 == 0:
        answer += (N // 5)
        N %= 5

        break

    N -= 3
    answer += 1

if N != 0:
    print(-1)
else:
    print(answer)


