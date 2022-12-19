from heapq import heappushpop, heappush

def solution(n, k, enemy):
    answer = 0
    if k >= len(enemy):
        answer = len(enemy)
        return answer
    heap = []
    total, cur_round = 0, 0

    for e in enemy:
        total += e
        if total <= n:
            heappush(heap, -e)
            cur_round += 1
        elif k > 0:
            k -= 1
            total += heappushpop(heap, -e)
            cur_round += 1
        else:
            break


    return cur_round