def solution(name):
    answer = 0
    
    alpha_dict = {chr(i+64):i for i in range(1,27)}
    
    min_move = len(name) - 1
    name_list = list(name)
    for idx, alpha in enumerate(name_list):
        if alpha <= 'N':
            answer += (alpha_dict[alpha] - 1)
        else:
            answer += (26 - alpha_dict[alpha] + 1)
        
        next = idx + 1
        while next < len(name) and name[next] == 'A':
            next += 1
            
        
        min_move = min([min_move, 2 *idx + len(name) - next, idx + 2 * (len(name) -next)])
        
    
        
    return answer + min_move