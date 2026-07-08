from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        max_area = 0

        # marking visited cells with -1

        def bfs(r, c):
            q = deque([[r,c]])
            grid[r][c] = -1
            area = 0
            while q:
                r, c = q.popleft()
                area += 1
                directions = [(0,1), (0,-1), (1,0), (-1,0)]
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if (min(nr, nc) >= 0
                    and nr < ROWS
                    and nc < COLS
                    and grid[nr][nc] == 1):
                        q.append([nr, nc])
                        grid[nr][nc] = -1
            return area
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    max_area = max(max_area, bfs(r,c))
        
        return max_area