class Solution:
    def connectSticks(self, sticks: List[int]) -> int:     

        heapq.heapify(sticks)
        res = 0
        while len(sticks) >= 2:
            x = heapq.heappop(sticks)
            y = heapq.heappop(sticks)
            heapq.heappush(sticks, x + y)
            res = res + x + y
        return res

        # use heap
        # always access min 2 elements