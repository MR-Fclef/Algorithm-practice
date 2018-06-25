# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
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
    def preorder(self, root, level, res):
        if root:
            if len(res) < level+1: res.append([])
            res[level].append(root.val)
            self.preorder(root.left, level+1, res)
            self.preorder(root.right, level+1, res)
    def levelOrder(self, root):
        res=[]
        self.preorder(root, 0, res)
        res.reverse()
        return res

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
test = Solution()
ro = test.buildTree(inorder,postorder)
re = test.levelOrder(ro)
print(re)

