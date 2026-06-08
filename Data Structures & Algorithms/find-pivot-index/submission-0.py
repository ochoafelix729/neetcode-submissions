class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0

        prefix_sum = [nums[0]] * len(nums)
        for i in range(1, len(nums)):
            prefix_sum[i] = prefix_sum[i-1] + nums[i]
        print(prefix_sum)
        
        for i in range(len(nums)):
            if i == 0:
                if prefix_sum[-1] - prefix_sum[0] == 0:
                    return i
            elif i == len(nums)-1:
                if prefix_sum[i-1] == 0:
                    return i
            else:
                if prefix_sum[-1] - prefix_sum[i] == prefix_sum[i-1]:
                    return i
        
        return -1
