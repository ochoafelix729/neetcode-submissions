class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        prev = res
        for i in range(1, len(nums)):
            cur = max(nums[i], prev + nums[i])
            res = max(res, cur)
            prev = cur
        return res