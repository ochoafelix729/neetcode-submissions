class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        surrounded_regions = []
        visited = set()

        def find_surrounding(r, c):
            if not (r in range(ROWS) and c in range(COLS)):
                return False
            if board[r][c] != 'O' or (r,c) in visited:
                return True
            
            visited.add((r,c))
            
            down = find_surrounding(r+1, c)
            up = find_surrounding(r-1, c)
            right = find_surrounding(r, c+1)
            left = find_surrounding(r, c-1)

            return down and up and right and left

        def capture_surrounding(r, c):
            local_visited = set()
            if (not (r in range(ROWS) and c in range(COLS))
                or board[r][c] != 'O' 
                or (r,c) in local_visited
            ):
                return
            
            board[r][c] = 'X'
            capture_surrounding(r+1, c)
            capture_surrounding(r-1, c)
            capture_surrounding(r, c+1)
            capture_surrounding(r, c-1)

        # find surrounded regions
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O' and (r,c) not in visited:
                    if find_surrounding(r, c):
                        surrounded_regions.append([r,c])
        
        # capture surrounded regions
        for r, c in surrounded_regions:
            capture_surrounding(r,c)
