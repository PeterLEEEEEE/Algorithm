def solution(lottos, win_nums):
    answer = []
    zero_cnt = lottos.count(0)
    hits = 0
    lo_score = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5}
    
    for num in lottos:
        if num in win_nums:
            hits += 1
    answer.append(lo_score.get(zero_cnt+hits, 6))
    answer.append(lo_score.get(hits, 6))
    
    return answer


l = [44, 1, 0, 0, 31, 25]
w_n = [31, 10, 45, 1, 6, 19]

print(solution(l, w_n))