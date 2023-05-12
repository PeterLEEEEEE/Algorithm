from collections import defaultdict, Counter

def solution(k, tangerine):
    answer = 0
    dic = Counter(tangerine)

    val_list = sorted(dic.values(), reverse=True)
    for i in val_list:
        k -= i
        answer += 1

        if k <= 0:
            return answer
    