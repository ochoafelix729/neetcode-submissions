from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        islands = 0
        
        # representing visited cells with '#'

        def bfs(r, c):
            q = deque([[r,c]])
            grid[r][c] = '#'
            while q:
                print(q)
                r, c = q.popleft()
                directions = [(1,0), (0,1), (-1,0), (0,-1)]
                for d in directions:
                    nr, nc = r+d[0], c+d[1]
                    if (min(nr,nc) >= 0
                    and nr < ROWS
                    and nc < COLS
                    and grid[nr][nc] == '1'):
                        q.append([nr,nc])
                        grid[nr][nc] = '#'
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    bfs(r,c)
                    islands += 1
        
        return islands
