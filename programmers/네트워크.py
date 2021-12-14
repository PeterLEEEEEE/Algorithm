def dfs(n, computers, pc, visited):
    visited[pc] = True
    for con in range(n):
        if con != pc and computers[pc][con] == 1:
            if visited[con] == False:
                dfs(n, computers, con, visited)

def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    for pc in range(n):
        if visited[pc] == False:
            dfs(n, computers, pc, visited)
            answer += 1
    return answer

if __name__ == '__main__':
    n = 3
    computers = [[1, 1, 0], 
                 [1, 1, 1], 
                 [0, 1, 1]]
    print(solution(n, computers))