# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfs(node):
            print(node.val)
            if not node.left and not node.right:
                if node.val == target:
                    print('removing', node.val)
                    return None
                return node
            
            if node.left:
                node.left = dfs(node.left)
            if node.right:
                node.right = dfs(node.right)

            if not node.left and not node.right and node.val == target:
                return None

            return node

        return dfs(root)

