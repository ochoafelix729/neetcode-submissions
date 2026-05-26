# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # dfs with current max visited passed as an argument
        goodnodes = 0

        def dfs(root, highest):
            nonlocal goodnodes
            if root is None: return 0

            if root.val >= highest:
                goodnodes += 1
                highest = root.val

            dfs(root.left, highest)
            dfs(root.right, highest)

        dfs(root, root.val)
        return goodnodes