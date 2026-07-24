# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = -1
        cur_k = 0
        def dfs(node):
            nonlocal res
            nonlocal cur_k
            if node is None:
                cur_k += 1
                return
            
            dfs(node.left)
            if cur_k == k:
                res = node.val
            dfs(node.right)

        dfs(root)
        return res

        