import math

def is_odd_num(num):
    for i in range(2, int(math.sqrt(num))+1):
        if int(num) % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    num_odd = []
    word = ''

    while n:
        word = str(n%k) + word
        n=n//k
    
    num_odd = word.split('0')
    print(num_odd)
    for num in num_odd:
        
        if len(num) == 0:
            continue
        if int(num) <= 1:
            continue
        
        if is_odd_num(int(num)):
            answer += 1
        
    # print(num_odd)
    return answer


n = 110011
k = 10

print(solution(n, k))