class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return []

        path = []
        stack = [root]

        while stack:
            cur = stack.pop()
            path.append(cur.val)

            # Push right first so left is processed first (LIFO)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
            
        return path