class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} # num -> index
        for i, num in enumerate(nums):
            if (target - num) in hashmap:
                if i < hashmap[target - num]:
                    return [i, hashmap[target - num]]
                else:
                    return [hashmap[target - num], i]
            hashmap[num] = i

       