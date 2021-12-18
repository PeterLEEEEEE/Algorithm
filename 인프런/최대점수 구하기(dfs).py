import sys
input = sys.stdin.readline

def DFS(L, sum, time):
    global res
    if time > m:
        return
    if L == n:
        if sum > res:
            res = sum
    else:
        DFS(L+1, sum+score[L], time+stime[L])
        DFS(L+1, sum, time)
        
if __name__ == '__main__':
    # 문제 개수 n, 제한 시간 m
    n, m = map(int, input().split())
    score = []
    stime = []
    for _ in range(n):
        s, t = map(int, input().split())
        score.append(s)
        stime.append(t)
    
    res = -1000

    DFS(0,0,0)

