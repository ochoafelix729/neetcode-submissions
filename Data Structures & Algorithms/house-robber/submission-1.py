class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        def dfs(i):
            if i >= len(nums):
                return 0

            if i in cache:
                return cache[i]
            
            opt1 = dfs(i+1) # skip current house
            opt2 = nums[i] + dfs(i+2) # rob current house and skip next house
            cache[i] = max(opt1, opt2)
            return cache[i]

        return max(dfs(0), dfs(1))