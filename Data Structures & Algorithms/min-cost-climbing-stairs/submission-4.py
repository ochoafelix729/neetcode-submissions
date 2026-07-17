class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # top-down DP approach
        cache = [-1] * (len(cost)+1)
        
        def dfs(i):
            if i >= len(cost):
                return 0
            
            if cache[i] != -1:
                return cache[i]

            cache[i] = cost[i] + min(dfs(i+1), dfs(i+2))
            return cache[i]
        
        return min(dfs(0), dfs(1))


        # brute force approach
        # O(2^n) time, O(n) space

        # def dfs(i, curCost):
        #     if i > len(cost):
        #         return float('inf')
        #     if i == len(cost):
        #         return curCost

        #     curCost += cost[i]
            
        #     # take one step
        #     step = dfs(i+1, curCost)

        #     # take two steps
        #     leap = dfs(i+2, curCost)

        #     return min(step, leap)
        
        # return min(dfs(0,0), dfs(1,0))