# 라이브러리 없이 다시 풀기

# from itertools import permutations

# N, M = map(int, input().split())
# P = permutations(range(1, N+1), M)

# for i in P:
#     print(' '.join(map(str, i)))


# 재귀
# 백트래킹 문제는 N이 10이내 
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
temp = []
visited = [False] * (n+1)

def cur(num):
    if num == m:
        print(' '.join(map(str, temp)))
        return
    for i in range(1, n+1):
        if visited[i] == False:
            visited[i] = True
            temp.append(i)
            cur(num+1)
            visited[i] = False
            temp.pop()
            
cur(0)