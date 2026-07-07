class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        path = [[False for _ in range(COLS)] for _ in range(ROWS)]

        def backtrack(row, col, letter_idx):
            if letter_idx == len(word):
                return True

            if row < 0 or col < 0 or row == ROWS or col == COLS:
                return False
            
            if path[row][col] or board[row][col] != word[letter_idx]:
                return False

            path[row][col] = True
            res = (
            backtrack(row+1, col, letter_idx+1) or
            backtrack(row-1, col, letter_idx+1) or
            backtrack(row, col+1, letter_idx+1) or
            backtrack(row, col-1, letter_idx+1))
            path[row][col] = False

            return res

        for i in range(ROWS):
            for j in range(COLS):
                if backtrack(i, j, 0):
                    return True
                    
        return False
