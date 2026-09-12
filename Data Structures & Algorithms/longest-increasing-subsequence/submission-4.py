class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            candidates = []
            for j in range(i):
                if nums[j] < nums[i]:
                    candidates.append(dp[j])
            if len(candidates) > 0:
                dp[i] = 1 + max(candidates)
        return max(dp)

    '''
    4 10 4 3 8 9
    1 2  1 1 
    '''