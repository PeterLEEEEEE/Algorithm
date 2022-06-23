from itertools import combinations_with_replacement as cwr
from collections import Counter


def solution(n, info):
    answer = []
    max_diff = 0
    info = info[::-1]
    for c in cwr(range(0, len(info)), n):
        ap_score = 0
        ryan_score = 0
        ryan_board = Counter(c)
        tmp = [0 for _ in range(len(info))]

        for i in range(0, len(info)):
            if info[i] < ryan_board[i]:
                ryan_score += i
            elif info[i] != 0:
                ap_score += i
            
            tmp[i] = ryan_board[i]

        if ryan_score > ap_score:
            diff = ryan_score - ap_score
            if max_diff < diff:
                max_diff = diff
                answer = tmp

    if answer:
        return answer[::-1]
    return [-1]


n = 5
info = [2,1,1,1,0,0,0,0,0,0,0]

print(solution(n, info))

