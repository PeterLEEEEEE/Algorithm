import itertools
N, M = map(int, input().split())


# C = itertools.combinations(range(1, N+1), M)

# for i in C:
#     print(' '.join(map(str, i)))
arr = []
def dfs(lev, temp):
    if lev == M:
        return 
    
    for j in range(j, N):
        dfs(lev+1)

dfs(0, "")

'''
N = 4, M = 1

'''