# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # solution 1: iterative DFS
        # time: O(n)
        # space: O(n)

        # stack = []
        # cur = root
        # while stack or cur:
        #     while cur:
        #         stack.append(cur)
        #         cur = cur.left
        #     cur = stack.pop()
        #     k -= 1
        #     if k == 0:
        #         return cur.val
        #     cur = cur.right

        # solution 2: inorder traversal (limited)
        # time: O(n)
        # space: O(n)
        arr = []
        def dfs(node):
            if node is None:
                return

            if len(arr) < k:
                dfs(node.left)
                if len(arr) < k:
                    arr.append(node.val)
                dfs(node.right)
        
        dfs(root)
        print(arr)
        return arr[-1]

        