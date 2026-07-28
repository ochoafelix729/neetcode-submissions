from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:

        # tabulation DP

        n = len(nums)

        if n == 1:
            return nums[0]

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])

        return dp[-1]


        # memo DP

        # @cache
        # def dfs(i):
        #     if i >= len(nums):
        #         return 0
            
        #     # skip
        #     skip = dfs(i+1)

        #     # rob
        #     rob = nums[i] + dfs(i+2)

        #     return max(skip, rob)
        
        # return max(dfs(0), dfs(1))