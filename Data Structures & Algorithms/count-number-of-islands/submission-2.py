class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        res = 0
        q = deque([])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    q.append((r,c))
                    grid[r][c] = '#'
                    while q:
                        r, c = q.popleft()
                        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                            if r+dr in range(ROWS) and c+dc in range(COLS) and grid[r+dr][c+dc] == '1':
                                q.append((r+dr, c+dc))
                                grid[r+dr][c+dc] = '#'
                    res += 1
        return res
