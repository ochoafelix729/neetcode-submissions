class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        cache = {}
        def dfs(i, cant_rob_last):
            if (i >= len(nums)) or (i == len(nums)-1 and cant_rob_last):
                return 0
            
            if (i, cant_rob_last) in cache:
                return cache[(i, cant_rob_last)]
            
            res = max(dfs(i+1, cant_rob_last), nums[i] + dfs(i+2, cant_rob_last))
            cache[(i, cant_rob_last)] = res
            return cache[(i, cant_rob_last)]
        
        return max(dfs(0, True), dfs(1, False))