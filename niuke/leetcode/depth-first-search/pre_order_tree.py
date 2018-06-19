# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        list = []
        self.iterative_preorder(root,list)
        return list
    def iterative_preorder(self, root, list):
        stack = []
        while root or stack:
            if root:
                list.append(root.val)
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                root = root.right
        return list
    
    def recursive_preorder(self, root, list):
        if root:
            list.append(root.val)
            self.preorder(root.left,list)
            self.preorder(root.right,list)


'''
解题思路：如果树为下图：

　　　　　　　　　　　　　　　　　　　　　　1

　　　　　　　　　　　　　　　　　　　　　/     \

　　　　　　　　　　　　　　　　　　　　2         3

　　　　　　　　　　　　　　　　　　　/     \    /    \

　　　　　　　　　　　　　　　　　　 4       5  6     7 

　　　　使用一个栈。步骤为：

　　　　一，先遍历节点1，并入栈，如果有左孩子，继续遍历并入栈，一直到栈为{1，2，4}。

　　　　二，开始弹栈，当栈顶元素为2时，弹出2，并检测2存在右孩子5，于是遍历5并入栈，此时栈为{1，5}。

　　　　三，弹出5，5没有左右孩子，继续弹栈，将1弹出后，栈为{}。

　　　　四，由于1存在右孩子，则继续按照以上步骤入栈出栈。{3, 6}->{7}->{}，结束。

　　　　栈的状态变化：{1}->{1,2}->{1,2,4}->{1,2}->{1}->{1,5}->{1}->{}->{3}->{3,6}->{3}->{}->{7}->{}。
'''