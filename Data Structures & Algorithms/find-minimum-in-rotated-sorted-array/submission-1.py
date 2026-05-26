class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        res = nums[0]
        while l <= r:
            mid = (l+r) // 2
            res = min(res, nums[mid])
            if nums[mid] > nums[r]:
                # min in right portion
                l = mid+1
            else:
                # min in left portion
                r = mid-1
        return res
                