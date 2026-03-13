import sys
input = sys.stdin.readline

def ri():    return int(input()) # 단일 정수
def rl():    return list(map(int, input().split())) # 정수 여러 개
def rm():    return map(int, input().split()) # 리스트
def rs():    return input().strip() # 문자열
def rsl():   return input().split() # 문자열 여러 개

def solve():      
    from collections import Counter                                                                         
    n = ri()                                                                               
    cards = Counter(rl())                                                                  
    m = ri()                           
    targets = rl()                                                                         
                                                                                            
    print(*[cards[t] for t in targets]) 

if __name__ == '__main__':
    solve()
