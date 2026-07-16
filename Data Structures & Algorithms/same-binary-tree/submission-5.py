# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # solution 1:
        # run dfs on both trees
        # keep track of paths
        # compare paths

        # def dfs(node, path):
        #     if node is None:
        #         path.append(None)
        #         return
            
        #     path.append(node.val)
            
        #     dfs(node.left, path)
        #     dfs(node.right, path)

        #     return path
        
        # return dfs(p,[]) == dfs(q, [])


        # solution 2:
        # run one dfs - keeping track of current node of each graph
        # if nodes ever differ -> early return False

        def dfs(p, q):
            if p is None and q is not None:
                return False
            if q is None and p is not None:
                return False
            if p is None and q is None:
                return True
            
            if p.val != q.val:
                return False
            
            res = dfs(p.left, q.left) and dfs(p.right, q.right)

            return res
        
        return dfs(p,q)
        
        
            
            


        
