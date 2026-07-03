class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        total_combs, cur_comb = [], []

        def backtrack(i, cur_sum):
            # base cases
            if cur_sum == target:
                total_combs.append(cur_comb.copy())
                return
            if i == len(nums) or cur_sum > target:
                return

            # include cur element and stay at i
            cur_comb.append(nums[i])
            backtrack(i, cur_sum + nums[i])
            cur_comb.pop()

            # don't include cur element
            backtrack(i+1, cur_sum)
        
        backtrack(0, 0)
        return total_combs