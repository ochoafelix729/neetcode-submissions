# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.balanced = True

    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if root is None:
                return 0

            l = dfs(root.left)
            r = dfs(root.right)

            if abs(l-r) > 1: self.balanced = False

            return 1 + max(l, r)

        dfs(root)
        return self.balanced

    