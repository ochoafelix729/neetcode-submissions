class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(i, nums):
            if i == len(nums):
                return [[]]
            
            res = []
            perms = dfs(i+1, nums)
            for p in perms:
                for j in range(len(p)+1):
                    pCopy = p.copy()
                    pCopy.insert(j, nums[i])
                    res.append(pCopy)
            
            return res

        return dfs(0, nums)
