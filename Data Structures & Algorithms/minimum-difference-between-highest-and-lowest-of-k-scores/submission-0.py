class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        minDifference = float('inf')
        for r in range(len(nums)):
            low = nums[l]
            high = nums[r]
            if r - l + 1 == k:
                minDifference = min(minDifference, nums[r] - nums[l])
                l += 1

        return minDifference