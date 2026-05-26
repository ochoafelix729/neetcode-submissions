# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.p_list = []
        self.q_list = []

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(root, tree):
            if root is None:
                self.p_list.append(None) if tree == 'p' else self.q_list.append(None)
                return None

            self.p_list.append(root.val) if tree == 'p' else self.q_list.append(root.val)

            dfs(root.left, tree)
            dfs(root.right, tree)
        
        dfs(p,'p')
        print(self.p_list)
        dfs(q,'q')
        print(self.q_list)
        return self.p_list == self.q_list