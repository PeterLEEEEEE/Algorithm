def solution(n):
    temp = n ** 0.5
    if temp ** 2 == n and int(temp) == temp:
        answer = (temp+1) ** 2
    else:
        answer = -1
    return answer