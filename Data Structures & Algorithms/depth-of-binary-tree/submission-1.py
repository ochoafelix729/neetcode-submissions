# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # recursive DFS
        # add depth of 1 for each call
        # take max of each branch
        
        if root is None: return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))