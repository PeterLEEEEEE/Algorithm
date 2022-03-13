def solution(clothes):
    answer = 1
    dic = {}
    for i in clothes:
        dic[i[1]] = dic.get(i[1], 0) + 1
    
    for val in dic.values():
        answer *= (val + 1)
    
    answer -= 1
    
    return answer