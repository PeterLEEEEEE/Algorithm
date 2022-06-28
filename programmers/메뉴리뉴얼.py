from collections import Counter
from itertools import combinations
def solution(orders, course):
    answer = []
    combs = {}
    for c in course:
        arr = []
        for order in orders:
            arr += combinations(sorted(order), c)
            
        cnt = Counter(arr)
        
        if cnt and max(cnt.values()) >= 2:
            for k, v in cnt.items():
                if v == max(cnt.values()):
                    answer.append(''.join(k))

    return sorted(answer)


# orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
# course = [2,3,5]

# print(solution(orders, course))

r = 'wxy'

arr = []

arr += combinations(r, 2)
print(arr)