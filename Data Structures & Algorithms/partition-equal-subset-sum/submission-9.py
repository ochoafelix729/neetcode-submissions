class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        # 0/1 knapsack top-down approach:

        summ = sum(nums)
        if summ % 2 == 1:
            return False
        
        capacity = summ // 2
        cache = [[-1] * (capacity+1) for _ in range(len(nums))]

        def dfs(i, rem):
            if rem == 0:
                return True
            if i == len(nums):
                return False

            if cache[i][rem] != -1:
                return cache[i][rem]
            
            # don't include
            left = dfs(i+1, rem)

            # include
            right = False
            if rem - nums[i] >= 0:
                right = dfs(i+1, rem-nums[i])
            
            cache[i][rem] = left or right
            return cache[i][rem]
        
        return dfs(0,capacity)

        # def sol1():


        '''
        standard DP top-down approach
        '''

            # summ = sum(nums)
            # if summ % 2 == 1:
            #     return False
            
            # target = summ // 2

            # cache = [[-1] * (target+1) for _ in range(len(nums))]

            # def dfs(i, curSum):
            #     if curSum == target:
            #         return True

            #     if i == len(nums) or curSum > target:
            #         return False
                
            #     if cache[i][curSum] != -1:
            #         return cache[i][curSum]
                
                
            #     # don't include
            #     left = dfs(i+1, curSum)
                
            #     # include
            #     right = dfs(i+1, curSum + nums[i])

            #     cache[i][curSum] = left or right

            #     return cache[i][curSum]

            # return dfs(0,0)
        
        
        

        
 
            

            

        
