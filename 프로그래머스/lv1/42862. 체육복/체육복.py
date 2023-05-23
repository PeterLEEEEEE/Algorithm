
def solution(n, lost, reserve):
    answer = 0
    stack = []
    
    r_dic = {i: 1 for i in reserve}
    l_dic = {i: 1 for i in lost}
    
    lost.sort()
    reserve.sort()
    
    for l in lost:
        if l in reserve:
            l_dic[l] = 0
            r_dic[l] = 0
            answer += 1
    for l in lost:
        if l_dic[l] == 0:
            continue
        for r in reserve:
            if l_dic[l] == 1 and r_dic[r] == 1:
                if l == r+1 or l == r-1:
                    r_dic[r] = 0
                    l_dic[l] = 0
                    answer += 1
                    break
    # for i in range(len(lost)):
    #     if lost[i] in reserve:
    #         dic[lost[i]] = 0
    #         answer += 1
    #         continue
    #     for r in reserve:
    #         if lost[i] == r+1 or lost[i] == r-1:
    #             if dic[r] == 1:
    #                 dic[r] = 0
    #                 answer += 1
    #                 break
                    
    
    return n - len(lost) + answer