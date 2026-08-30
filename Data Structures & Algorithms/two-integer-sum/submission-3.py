class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {num: i for i, num in enumerate(nums)}
        
        for i, num in enumerate(nums):
            if (target - num) in hashmap and hashmap[target - num] != i:
                small, large = min(i, hashmap[target - num]), max(i, hashmap[target - num])
                return [small, large]