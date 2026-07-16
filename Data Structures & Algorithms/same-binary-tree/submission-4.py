# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # run dfs on both trees
        # keep track of paths
        # compare paths

        def dfs(node, path):
            if node is None:
                path.append(None)
                return
            
            path.append(node.val)
            
            dfs(node.left, path)
            dfs(node.right, path)

            return path
        
        return dfs(p,[]) == dfs(q, [])
        
