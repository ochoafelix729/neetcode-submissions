class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
         0 0 2 0 1
         2 0 0 0 1
         2 1 0 0 0 
        '''

        l, r = 0, 1
        while r < len(nums):
            if nums[l] != 0:
                l += 1
            if nums[l] == 0 and nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            r += 1

        return nums
        