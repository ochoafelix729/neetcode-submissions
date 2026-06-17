from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []

        q = deque([root])
        levels = [[root.val]]
        while q:
            level = []
            for _ in range(len(q)):
                cur = q.popleft()
                if cur:
                    if cur.left:
                        q.append(cur.left)
                        level.append(cur.left.val)
                    if cur.right:
                        q.append(cur.right)
                        level.append(cur.right.val)
            if level:
                levels.append(level)
            
        return levels




            