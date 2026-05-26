class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1

        high = float('-inf')
        while r > l:
            area = min(heights[l], heights[r]) * (r-l) 
            high = max(high, area)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return high