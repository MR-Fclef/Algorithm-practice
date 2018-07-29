# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def maxDepthHelper(root):
            if not root: return 0
            return max(maxDepthHelper(root.left), maxDepthHelper(root.right))+1

        return maxDepthHelper(root)