class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        cache = {}

        def dfs(i, prev):
            if i == n:
                return 0
            
            if (i,prev) in cache:
                return cache[(i,prev)]

            LIS = dfs(i+1, prev) # don't include cur element
            
            if prev == -1 or nums[i] > nums[prev]:
                LIS = max(LIS, 1 + dfs(i+1, i)) # include cur element

            cache[(i,prev)] = LIS

            return cache[(i,prev)]
        
        return dfs(0,-1)
            