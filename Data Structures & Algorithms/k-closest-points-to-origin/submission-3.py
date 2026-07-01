import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(p: List[int]) -> float:
            return math.sqrt(p[0] ** 2 + p[1] ** 2)
        
        points_and_distances = []
        for point in points:
            dist = distance(point)
            points_and_distances.append((dist, point))
        
        k_closest = []
        minHeap = points_and_distances
        heapq.heapify(minHeap)
        for _ in range(k):
            k_closest.append(heapq.heappop(minHeap)[1])
        return k_closest