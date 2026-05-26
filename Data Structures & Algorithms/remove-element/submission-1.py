class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums)
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.remove(nums[i])
                k -= 1
                i -= 1
            i += 1
        return k