def solution(s):

    answer = len(s)
    limit = len(s) // 2
    str_cnt = 1
    
    for i in range(1, limit):
        part_len = len(s[:i])
        str_part = s[:part_len]
        str_total = ''
        

        for j in range(part_len, len(s)+part_len, part_len):
            
            if str_part == s[j:j+part_len]:
                str_cnt += 1
            
            else:
                
                if str_cnt > 1:
                    str_total += (str(str_cnt) + str_part)
                else:
                    str_total += str_part
                
                str_cnt = 1
                str_part = s[j:j+part_len]
            
            
        
        if len(str_total) <= answer:
            answer = len(str_total)

    
    return answer



s = "abcabcabcabcdededededede"
solution(s)
