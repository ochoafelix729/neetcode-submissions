class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def xor(arr):
            res = 0
            for el in arr:
                res ^= el
            return res
        
        def find_subsets(i, curSet):
            nonlocal subsets

            if i == len(nums):
                subsets.append(curSet.copy())
                return
            
            # include
            curSet.append(nums[i])
            find_subsets(i+1, curSet)
            curSet.pop()

            # don't include
            find_subsets(i+1, curSet)
        
        subsets = []
        find_subsets(0, [])

        xor_sum = 0
        for ss in subsets:
            xor_sum += xor(ss)
        
        return xor_sum

        