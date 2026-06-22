class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)
        res = r

        def canSplit(largestSum: int) -> bool:
            cur_sum = largestSum
            subarrays = 1
            for n in nums:
                if cur_sum - n < 0:
                    subarrays += 1
                    cur_sum = largestSum
                    if subarrays > k:
                        return False
                cur_sum -= n
            return True
        
        while l <= r:
            largestSum = (l+r) // 2
            if canSplit(largestSum):
                res = min(res, largestSum)
                r = largestSum - 1
            else:
                l = largestSum + 1
        
        return res