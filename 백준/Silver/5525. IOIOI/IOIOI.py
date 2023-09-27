import sys


input = sys.stdin.readline


def solution(N):
    cnt, ans = 0, 0
    target = 'IOI'
    if N > 1:
        target += 'OI' * (N - 1)

    len_tar = len(target)
    i = 0

    while i < M-1:
        if S[i:i+3] == 'IOI':
            cnt += 1
            if cnt == N:
                ans += 1
                cnt -= 1
            i += 2

        else:
            i += 1
            cnt = 0

    return ans

if __name__ == '__main__':
    # write input
    N = int(input())
    M = int(input())
    S = input()

    print(solution(N))