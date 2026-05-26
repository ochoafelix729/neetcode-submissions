# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSame(self, r1, r2):
        if not r1 and not r2:
            return True
        
        if r1 and r2 and r1.val == r2.val:
            return (self.isSame(r1.left, r2.left)
            and self.isSame(r1.right, r2.right))

        return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is None:
            return True
        
        if root is None and subRoot:
            return False
        
        if root is None:
            return False
        
        if self.isSame(root, subRoot):
            return True
        
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))




