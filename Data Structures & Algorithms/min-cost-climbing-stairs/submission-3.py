class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # top-down DP approach
        cache = [[-1] * (sum(cost)+1) for _ in range(len(cost)+1)]
        
        def dfs(i, curCost):
            if i > len(cost):
                return float('inf')
            if i == len(cost):
                return curCost

            if cache[i][curCost] != -1:
                return cache[i][curCost]

            curCost += cost[i]
            
            # take one step
            step = dfs(i+1, curCost)

            # take two steps
            leap = dfs(i+2, curCost)

            cache[i][curCost] = min(step, leap)
            return cache[i][curCost]
        
        return min(dfs(0,0), dfs(1,0))


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