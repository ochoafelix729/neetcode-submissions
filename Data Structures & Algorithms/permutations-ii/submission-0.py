class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        perms, perm = [], []
        visited = [False] * len(nums)

        def backtrack():
            # base case
            if len(perm) == len(nums):
                perms.append(perm.copy())
                return
            
            for i in range(len(nums)):
                if visited[i] or (i > 0 and nums[i] == nums[i-1] and not visited[i-1]):
                    continue
                
                visited[i] = True
                perm.append(nums[i])
                backtrack()
                perm.pop()
                visited[i] = False

        backtrack()
        return perms
                    
                


        
        backtrack()
        return perms