class Solution:
    def climbStairs(self, n: int) -> int:

        # bottom-up DP approach
        # O(n) time, O(n) space
        
        if n <= 2:
            return n

        dp = [0] * (n+1)
        dp[1], dp[2] = 1, 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]

        
        # top-down DP approach
        # O(n) time, O(n) space
        
        # cache = [-1] * n

        # def dfs(i):
        #     if i >= n:
        #         return 1
            
        #     if cache[i] != -1:
        #         return cache[i]

        #     step = dfs(i+1)
        #     leap = dfs(i+2)
        #     cache[i] = step + leap
        #     return cache[i]
        
        # return dfs(1)