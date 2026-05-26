class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {num: i for i, num in enumerate(nums)}

        for i, num in enumerate(nums):
            if (target-num) in table and i != table[target-num]:
                return [min(table[target-num], i), max(table[target-num], i)]