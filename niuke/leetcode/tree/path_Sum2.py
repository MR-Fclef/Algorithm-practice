# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    pre = []
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        def path(root,currsum,arr):
            if root.left==None and root.right==None:
                if currsum == sum: res.append(arr)
            if root.left: path(root.left,currsum+root.left.val,arr+[root.left.val])
            if root.right: path(root.right,currsum+root.right.val,arr+[root.right.val])

        res = []
        if root == None:
            return []
        path(root,root.val,[root.val])
        return res
    def preorder(self,root):
        if root == None:
            return
        self.pre.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)
        return self.pre
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
test = Solution()
postorder = [7,2,11,4,13,5,1,4,8,5]
inorder = [7,11,2,4,5,13,8,5,4,1]
root = test.buildTree(inorder,postorder)
print(test.preorder(root))
result = test.pathSum(root,22)
print(result)
