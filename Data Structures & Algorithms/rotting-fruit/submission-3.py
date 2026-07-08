from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        minutes, fresh = 0, 0
        q = deque([])

        # find number of fresh fruits
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append([r,c])

        # multi-source BFS
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        while fresh > 0 and q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if (min(nr, nc) >= 0
                        and nr < ROWS
                        and nc < COLS
                        and grid[nr][nc] == 1
                    ):
                        q.append([nr,nc])
                        grid[nr][nc] = 2
                        fresh -= 1
            minutes += 1

        return minutes if fresh == 0 else -1
        
        
        