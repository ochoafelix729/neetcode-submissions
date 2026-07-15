"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
            
        intervals.sort(key=lambda x: x.start)
        minheap = [intervals[0].end]
        for i in range(1, len(intervals)):
            print(minheap)
            if minheap and intervals[i].start >= minheap[0]:
                heapq.heappop(minheap)
            heapq.heappush(minheap, intervals[i].end)

        return len(minheap)
        