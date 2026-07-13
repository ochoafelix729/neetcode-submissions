class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        cache = {}
        n = len(nums)
        def dfs(i, flag):
            if i >= len(nums) or (flag and i == n-1):
                return 0

            if (i,flag) in cache:
                return cache[(i,flag)]

            opt1 = dfs(i+1, flag) # include first and exclude last
            opt2 = nums[i] + dfs(i+2, flag) # exclude first and last allowed

            cache[(i,flag)] = max(opt1, opt2)
            return cache[(i,flag)]

        # we flag whether the last house is banned
        return max(dfs(0, True), dfs(1, False))