from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        # memo DP

        @cache
        def dfs(i):
            if i >= len(nums):
                return 0
            
            # skip
            skip = dfs(i+1)

            # rob
            rob = nums[i] + dfs(i+2)

            return max(skip, rob)
        
        return max(dfs(0), dfs(1))