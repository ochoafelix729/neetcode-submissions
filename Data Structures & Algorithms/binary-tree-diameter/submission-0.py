# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        longest = 0

        def dfs(node):
            nonlocal longest
            if node is None: return 0
            l = dfs(node.left)
            r = dfs(node.right)
            longest = max(longest, l+r)
            return 1 + max(l, r)

        dfs(root)
        return longest
