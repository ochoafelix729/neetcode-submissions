# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node, blocked, cache):
            if node is None:
                return 0
            
            if (node, blocked) in cache:
                return cache[(node, blocked)]

            if blocked:
                cache[(node, blocked)] = dfs(node.left, False, cache) + dfs(node.right, False, cache)
            
            else:
                cache[(node, blocked)] = max(
                    node.val + dfs(node.left, True, cache) + dfs(node.right, True, cache),
                    dfs(node.left, False, cache) + dfs(node.right,False, cache)
                )

            return cache[(node, blocked)]

        return max(
            dfs(root, False, defaultdict(int)), 
            dfs(root.left, False, defaultdict(int)), 
            dfs(root.right, False, defaultdict(int))
        )

