# 내 답안
def solution(participant, completion):
    dic = {}
    for part in participant:
        dic[part] = dic.get(part, 0) + 1
    
    for c in completion:
        dic[c] -= 1
    
    for i in dic:
        if dic[i] == 1:
            return i
        


