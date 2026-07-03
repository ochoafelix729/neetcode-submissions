class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets, cur_set = [], []

        def backtrack(i):
            # base case
            if i == len(nums):
                subsets.append(cur_set.copy())
                return
            
            # add cur element
            cur_set.append(nums[i])
            backtrack(i+1)
            cur_set.pop()

            # don't add cur element
            while i < len(nums)-1 and nums[i] == nums[i+1]:
                i += 1
            backtrack(i+1)
        
        backtrack(0)
        return subsets