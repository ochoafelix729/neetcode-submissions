class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = len(nums)+1
        l = 0
        window_sum = 0
        for r in range(len(nums)):
            window_sum += nums[r]
            while l <= r and window_sum >= target:
                res = min(res, r - l + 1)
                window_sum -= nums[l]
                l += 1
        return res if res != len(nums)+1 else 0