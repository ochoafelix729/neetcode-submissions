# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        prev = None
        cur = root
        while cur and cur.val != key:
            if cur.val < key:
                prev = cur
                cur = cur.right
            else:
                prev = cur
                cur = cur.left
        if not cur:
            return root
        

        # case 1: no children
        if not cur.left and not cur.right:
            if cur == root:
                root = None
            elif cur == prev.left:
                prev.left = None
            else:
                prev.right = None

        # case 2: left child only
        elif cur.left and not cur.right:
            if cur == root:
                root = cur.left
            elif cur == prev.left:
                prev.left = cur.left
            else:
                prev.right = cur.left

        # case 3: right child only
        elif cur.right and not cur.left:
            if cur == root:
                root = cur.right
            elif cur == prev.left:
                prev.left = cur.right
            else:
                prev.right = cur.right

        # case 4: both children
        else:
            succ_prev = cur
            succ = cur.right
            while succ.left:
                succ_prev = succ
                succ = succ.left
            
            if succ_prev != cur:
                succ_prev.left = succ.right
                succ.right = cur.right
            
            succ.left = cur.left
            
            if cur == root:
                root = succ
            elif cur == prev.left:
                prev.left = succ
            else:
                prev.right = succ
            
        return root



