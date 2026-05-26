# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return []

        # original: cur - right - left
        # reversed: left - right - cur
        
        path = []
        stack = [root]
        cur = root

        while stack:
            cur = stack.pop()
            path.append(cur.val)

            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)       

        return path[::-1]