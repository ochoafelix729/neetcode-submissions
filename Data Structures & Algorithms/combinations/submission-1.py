class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(i, curComb):
            nonlocal res

            if len(curComb) == k:
                res.append(curComb.copy())
                return
            if i > n:
                return
            
            # include
            curComb.append(i)
            backtrack(i+1, curComb)
            curComb.pop()

            # don't include
            backtrack(i+1, curComb)

        res = []
        backtrack(1, [])
        return res
