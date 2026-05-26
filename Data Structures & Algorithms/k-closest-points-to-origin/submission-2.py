import heapq

class Solution:
    def dist(self, x: int, y: int) -> float:
        return ((abs(x) ** 2) + (abs(y) ** 2)) ** (1/2)
  
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            dist = self.dist(point[0], point[1])
            heapq.heappush(heap, (-dist, point))
            if len(heap) > k:
                heapq.heappop(heap)
                
        return [point for (_, point) in heap]