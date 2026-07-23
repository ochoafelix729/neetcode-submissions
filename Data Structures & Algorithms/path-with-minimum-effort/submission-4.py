class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # djikstra's

        ROWS = len(heights)
        COLS = len(heights[0])

        minCost = [[float('inf') for _ in range(COLS)] for _ in range(ROWS)]
 
        for r in range(ROWS):
            for c in range(COLS):
                minCost[r][c] = float('inf')
        
        minheap = [(0, 0, 0)] # effort, row, column
        visited = set()
        maxDiff = 0
        totalDiff = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while minheap:
            e1, r, c = heapq.heappop(minheap)
            if e1 > minCost[r][c]:
                continue

            totalDiff += e1
            maxDiff = max(maxDiff, e1)

            if r == ROWS - 1 and c == COLS - 1:
                break
            source_height = heights[r][c]
            heights[r][c] = '#'
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr not in range(ROWS) or nc not in range(COLS) or heights[nr][nc] == '#':
                    continue
                diff = abs(heights[nr][nc] - source_height)
                if  diff < minCost[nr][nc]:
                    heapq.heappush(minheap, (diff, nr, nc))
                    minCost[nr][nc] = diff
 
        return maxDiff