# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            return self.dfs(root.left, root.right)
        return True
    def dfs(self, p, q):
        if p == None and q == None: return True
        if p and q and p.val == q.val:
            return self.dfs(p.right, q.left) and self.dfs(p.left, q.right)
        return False