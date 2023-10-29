'''
1. 같은 행에 배치 금지
2. 같은 열 금지
3. 같은 대각선 금지
'''

import sys


input = sys.stdin.readline

def checkPath(lev):
    for i in range(lev):
        if (board[lev] == board[i]) or abs(board[lev] - board[i]) == lev - i:
            return False
    return True


def solution(lev):
    global ans

    if lev == N:
        ans += 1
    else:
        for i in range(N):
            board[lev] = i

            if checkPath(lev):
                solution(lev+1)

if __name__ == '__main__':
    # write input
    N = int(input())
    board = [0] * N
    ans = 0

    solution(0)
    print(ans)