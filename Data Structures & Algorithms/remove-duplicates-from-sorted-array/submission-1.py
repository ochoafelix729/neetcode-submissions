class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 1
        res = 1
        while r < len(nums):
            while r < len(nums) and nums[r] == nums[l]:
                r += 1
            l += 1
            if r < len(nums):
                nums[l] = nums[r]
                res += 1
        
        return res