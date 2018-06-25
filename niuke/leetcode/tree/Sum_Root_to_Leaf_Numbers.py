# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    pre = []
    def pathSum(self, root):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        def path(root,currsum,arr):
            sum_arr = 0
            if root.left==None and root.right==None:
                for i in range(0,len(arr)):
                    sum_arr += arr[i]*(10**(len(arr)-i-1))
                res.append(sum_arr)
            if root.left: path(root.left,currsum+root.left.val,arr+[root.left.val])
            if root.right: path(root.right,currsum+root.right.val,arr+[root.right.val])

        res = []
        if root == None:
            return []
        path(root,root.val,[root.val])
        return res
    def sum_path(self,res):
        return sum(res)
                
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
postorder = [5,1,9,0,4]
inorder = [5,9,1,4,0]
root = test.buildTree(inorder,postorder)
print(test.preorder(root))
result = test.pathSum(root)
print(test.sum_path(result))

'''
AC_code
'''
# class Solution(object):
#     def sumNumbers(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         return sum(self.path_Has(root))
    
#     def path_Has(self,root):
#         def path(root,currsum,arr):
#             sum_arr = 0
#             if root.left==None and root.right==None:
#                 for i in range(0,len(arr)):
#                     sum_arr += arr[i]*(10**(len(arr)-i-1))
#                 res.append(sum_arr)
#             if root.left: path(root.left,currsum+root.left.val,arr+[root.left.val])
#             if root.right: path(root.right,currsum+root.right.val,arr+[root.right.val])

#         res = []
#         if root == None:
#             return []
#         path(root,root.val,[root.val])
#         return res