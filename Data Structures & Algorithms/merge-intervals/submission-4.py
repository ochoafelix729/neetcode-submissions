class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        curInterval = intervals[0]
        for start, end in intervals[1:]:
            if start <= curInterval[1]:
                curInterval[1] = max(curInterval[1], end)
            else:
                res.append(curInterval)
                curInterval = [start, end]
        res.append(curInterval)
        return res
            
