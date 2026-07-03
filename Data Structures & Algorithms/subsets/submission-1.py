class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets, cur_set = [], []
        def backtrack(i, nums, subsets, cur_set):
            # base case
            if i == len(nums):
                subsets.append(cur_set.copy())
                return
            
            # include cur element
            cur_set.append(nums[i])
            backtrack(i+1, nums, subsets, cur_set)

            # don't include cur element
            cur_set.pop()
            backtrack(i+1, nums, subsets, cur_set)

        backtrack(0, nums, subsets, cur_set)
        return subsets
