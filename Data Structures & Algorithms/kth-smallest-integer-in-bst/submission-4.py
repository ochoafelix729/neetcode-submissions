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

        # solution 2: inorder traversal
        # time: O(n)
        # space: O(h)
        res = 0
        cnt = 0
        def dfs(node, k):
            nonlocal res
            nonlocal cnt

            if node is None:
                return
            if cnt == k:
                return

            dfs(node.left, k)
            cnt += 1
            if cnt == k:
                res = node.val
                print(res)
            dfs(node.right, k)
        
        dfs(root, k)
        return res

        