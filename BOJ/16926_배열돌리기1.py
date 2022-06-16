import sys
from collections import deque


input = sys.stdin.readline
N, M, R = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
move = [[1, 0], [0, 1], [-1, 0], [0, -1]]

q = deque()

def rotate(R):
    q = deque()
    for depth in range(min(N, M) // 2):
        r = c = depth

        for dr, dc in move:  
            while True:
                nr = r + dr
                nc = c + dc
                if depth <= nr < N - depth and depth <= nc < M - depth:
                    q.append(arr[r][c])
                    r = nr
                    c = nc
                else:
                    break
        
        q.rotate(R)

        for dr, dc in move: 
            while True:
                nr = r + dr
                nc = c + dc
                if depth <= nr < N - depth and depth <= nc < M - depth:
                    arr[r][c]=q.popleft()
                    r = nr
                    c = nc
                else:
                    break

rotate(R)

for i in range(N):
    print(*arr[i])
