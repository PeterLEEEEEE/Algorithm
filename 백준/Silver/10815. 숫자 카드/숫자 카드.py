import sys
input = sys.stdin.readline

def ri():    return int(input()) # 단일 정수
def rl():    return list(map(int, input().split())) # 정수 여러 개
def rm():    return map(int, input().split()) # 리스트
def rs():    return input().strip() # 문자열
def rsl():   return input().split() # 문자열 여러 개

def solve(cards, targets):
    result = [int(t in cards) for t in targets]
    
    print(*result)
    
if __name__ == '__main__':
    n = ri()
    cards = set(rl())
    m = ri()
    targets = rl()
    
    solve(cards, targets)
