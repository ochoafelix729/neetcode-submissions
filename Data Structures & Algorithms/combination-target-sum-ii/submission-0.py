class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        total_combs, cur_comb = [], []

        def backtrack(i, cur_sum):
            # base cases
            if cur_sum == target:
                total_combs.append(cur_comb.copy())
                return
            if i == len(candidates) or cur_sum > target:
                return
            
            # include cur element
            cur_comb.append(candidates[i])
            backtrack(i+1, cur_sum + candidates[i])
            cur_comb.pop()

            # don't include cur element
            while i < len(candidates)-1 and candidates[i] == candidates[i+1]:
                i += 1
            backtrack(i+1, cur_sum)
        
        backtrack(0, 0)
        return total_combs
