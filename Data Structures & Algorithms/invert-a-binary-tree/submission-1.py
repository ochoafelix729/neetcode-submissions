# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # for each level (BFS)
            # for each node
                # node.left = node.right
                # node.right = node.left

        if root is None: return None

        queue = [root]
        while queue:
            # update traversal
            node = queue.pop(0)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)

            # switch child node pointers
            temp = node.left if node.left else None
            node.left = node.right if node.right else None
            node.right = temp
        
        return root
    