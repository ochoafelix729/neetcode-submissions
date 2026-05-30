class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consec = 0
        consec = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                consec += 1
                max_consec = max(max_consec, consec)
            else:
                consec = 0
        return max_consec
