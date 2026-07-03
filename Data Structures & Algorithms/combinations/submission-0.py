class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        total_combs, cur_comb = [], []

        def backtrack(i, n, k, total_combs, cur_comb):
            # base cases
            if len(cur_comb) == k:
                total_combs.append(cur_comb.copy())
                return
            if i > n:
                return
            
            # include cur element
            cur_comb.append(i)
            backtrack(i+1, n, k, total_combs, cur_comb)

            # don't include cur element
            cur_comb.pop()
            backtrack(i+1, n, k, total_combs, cur_comb)
        
        backtrack(1, n, k, total_combs, cur_comb)
        return total_combs