class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        def backtrack(i, xorr):
            nonlocal res

            if i == len(nums):
                res += xorr
                return
            
            # include
            backtrack(i+1, xorr ^ nums[i])

            # don't include
            backtrack(i+1, xorr)
        
        res = 0
        backtrack(0, 0)
        return res
        

        