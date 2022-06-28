from collections import deque

class Solution:
    
    
    def numIslands(self, grid) -> int:
        ans = 0
        def bfs(i, j):
            dy = [1, -1, 0, 0]
            dx = [0, 0, 1, -1]

            q = deque()
            q.append([i, j])
            
            while q:
                y, x = q.popleft()
                
                for i in range(4):
                    ny = dy[i] + y
                    nx = dx[i] + x

                    if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]) and grid[ny][nx] == '1':
                        grid[ny][nx] = '0'
                        q.append([ny, nx])
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    bfs(i, j)
                    ans += 1
        
        return ans