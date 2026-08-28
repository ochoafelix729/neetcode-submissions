class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        rowZero = False

        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True
        
        for r in range(1, m):
            if matrix[r][0] == 0:
                for i in range(n):
                    matrix[r][i] = 0
        
        for c in range(n):
            if matrix[0][c] == 0:
                for i in range(m):
                    matrix[i][c] = 0
        
        if rowZero:
            for i in range(n):
                matrix[0][i] = 0


        # m, n = len(matrix), len(matrix[0])

        # # find initial 0's
        # zeroes = []
        # for r in range(m):
        #     for c in range(n):
        #         if matrix[r][c] == 0:
        #             zeroes.append((r,c))
        
        # rows = set()
        # cols = set()
        # for r, c in zeroes:
        #     # up/down fill
        #     if c not in cols:
        #         i = 0
        #         while i in range(m):
        #             matrix[i][c] = 0
        #             i += 1
        #         cols.add(c)

        #     # left/right fill
        #     if r not in rows:
        #         j = 0
        #         while j in range(n):
        #             matrix[r][j] = 0
        #             j += 1
        #         rows.add(r)


        