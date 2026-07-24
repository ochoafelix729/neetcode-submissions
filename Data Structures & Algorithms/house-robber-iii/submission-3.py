# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        cache = defaultdict(int)
        def dfs(node, blocked):
            if node is None:
                return 0

            state = (node, blocked)
            if state in cache:
                return cache[state]

            if blocked:
                cache[state] = dfs(node.left, False) + dfs(node.right, False)
            
            else:
                cache[state] = max(
                    node.val + dfs(node.left, True) + dfs(node.right, True),
                    dfs(node.left, False) + dfs(node.right,False)
                )

            return cache[state]

        return dfs(root, False)
