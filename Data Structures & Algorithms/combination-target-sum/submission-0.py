class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, sol = [], []
        n = len(nums)
        cur_sum = 0

        def backtrack(i, cur_sum):
            if cur_sum == target:
                res.append(sol[:])
                return
            
            if i == n or cur_sum > target:
                return

            # go left
            sol.append(nums[i])
            backtrack(i, cur_sum + nums[i])
            sol.pop()

            # go right
            backtrack(i+1, cur_sum)
        
        backtrack(0, cur_sum)
        return res
