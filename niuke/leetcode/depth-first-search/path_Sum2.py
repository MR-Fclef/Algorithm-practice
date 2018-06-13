# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    re = []
    arr = []
    def pathSum(self, root, sum,arr):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        arr.append(root.val)
        if root == None:
            return False
        if root.left ==None and root.right ==None and (sum-root.val)==0:
            return re.append(arr)
        return self.hasPathSum(root.left,sum-root.val,arr) or self.hasPathSum(root.right,sum-root.val,arr)
    
    def buildTree(self, inorder, postorder):
        if len(inorder) == 0:
            return None
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        root = TreeNode(postorder[len(postorder) - 1])
        index = inorder.index(postorder[len(postorder) - 1])
        root.left = self.buildTree(inorder[ 0 : index ], postorder[ 0 : index ])
        root.right = self.buildTree(inorder[ index + 1 : len(inorder) ], postorder[ index : len(postorder) - 1 ])
        return root

