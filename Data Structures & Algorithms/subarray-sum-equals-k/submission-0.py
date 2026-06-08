class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # prefix: 2 1 2 4
        #   nums: 2 -1 1 2

        if len(nums) == 1:
            return 1 if nums[0] == k else 0
        
        prefix_map = {
            0 : 1
        }
        
        subarrays = 0
        prefix_sum = 0
        for i, n in enumerate(nums):
            prefix_sum += n
            if prefix_sum - k in prefix_map:
                subarrays += prefix_map[prefix_sum-k]
            if prefix_sum not in prefix_map:
                prefix_map[prefix_sum] = 1
            else:
                prefix_map[prefix_sum] += 1

        return subarrays
            
                
