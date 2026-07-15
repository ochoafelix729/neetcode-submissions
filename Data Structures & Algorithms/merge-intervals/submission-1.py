class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals

        intervals.sort(key=lambda x: x[0])
        res = []
        prev = 0
        i = 1
        while i < len(intervals):
            if intervals[i][0] <= intervals[prev][1]:
                while i < len(intervals) and intervals[i][0] <= intervals[prev][1]:
                    # merge
                    intervals[prev][1] = max(intervals[prev][1], intervals[i][1])
                    i += 1
            
            else:
                res.append(intervals[prev])
                prev = i
                i += 1

        res.append(intervals[prev])
            
        
        return res

         # [1,5], [1,5], [6,7]       
            
