# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def right(level):
            if len(level) == 0:
                return []
            return [level[-1].val]+right([x for i in level for x in [i.left,i.right] if x])
        if not root:
            return []
        return right([root])
