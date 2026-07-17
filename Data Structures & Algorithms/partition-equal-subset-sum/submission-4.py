class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summ = sum(nums)
        if summ % 2 == 1:
            return False
        
        target = summ // 2

        cache = [[-1] * (target+1) for _ in range(len(nums))]

        def dfs(i, curSum):
            if curSum == target:
                return True

            if i == len(nums) or curSum > target:
                return False
            
            if cache[i][curSum] != -1:
                return cache[i][curSum]
            
            
            # don't include
            left = dfs(i+1, curSum)
            
            # include
            right = dfs(i+1, curSum + nums[i])

            cache[i][curSum] = left or right

            return cache[i][curSum]

        return dfs(0,0)
            

            

        
