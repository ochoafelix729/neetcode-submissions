class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        def backtrack(i, curSet, xorr):
            nonlocal res

            if i == len(nums):
                res += xorr
                return
            
            
            # include
            curSet.append(nums[i])

            xorr = 0
            for el in curSet:
                xorr ^= el

            backtrack(i+1, curSet, xorr)
            curSet.pop()

            xorr = 0
            for el in curSet:
                xorr ^= el

            # don't include
            backtrack(i+1, curSet, xorr)
        
        res = 0
        backtrack(0, [], 0)
        return res
        

        