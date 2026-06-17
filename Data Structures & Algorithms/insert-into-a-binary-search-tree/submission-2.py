# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def findParent(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        cur = root
        while cur.left or cur.right:
            if val < cur.val:
                if not cur.left:
                    return cur
                cur = cur.left
            else:
                if not cur.right:
                    return cur
                cur = cur.right
        return cur


    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)

        parent = self.findParent(root, val)
        if val > parent.val:
            parent.right = TreeNode(val)
        else:
            parent.left = TreeNode(val)

        return root




