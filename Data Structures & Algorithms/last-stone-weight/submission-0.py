import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1: return stones[0]
        heapq.heapify_max(stones)
        while len(stones) > 1:
            y = heapq.heappop_max(stones)
            x = heapq.heappop_max(stones)
            print(x,y)
            if x < y:
                heapq.heappush_max(stones, y-x)
            print(stones)

        return stones[0] if stones else 0