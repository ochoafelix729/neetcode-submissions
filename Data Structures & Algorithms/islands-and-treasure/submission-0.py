from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        ROWS = len(grid)
        COLS = len(grid[0])

        q = deque([])
        visited = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visited.add((r,c))

        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        dist = 1
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if (nr in range(ROWS) and
                        nc in range(COLS) and
                        grid[nr][nc] == INF and
                        (nr,nc) not in visited
                    ):
                        q.append([nr,nc])
                        visited.add((nr,nc))
                        grid[nr][nc] = dist
            dist += 1
        
        
