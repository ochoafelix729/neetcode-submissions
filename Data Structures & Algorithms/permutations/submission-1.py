class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms, perm = [], []
        visited = [False] * len(nums)

        def backtrack():
            # base case
            if len(perm) == len(nums):
                perms.append(perm.copy())
                return
            
            for i in range(len(nums)):
                if visited[i]:
                    continue
                
                visited[i] = True
                perm.append(nums[i])
                backtrack()
                perm.pop()
                visited[i] = False
        
        backtrack()
        return perms