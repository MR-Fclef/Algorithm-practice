class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def pre_order(tree):
    if tree==None:
        print('#')
        return 
    print(tree.val)
    pre_order(tree.left)
    pre_order(tree.right)

class Solution:
    # @return a list of tree node
    def dfs(self, start, end):
        if start > end: return [None]
        res = []
        for rootval in range(start, end+1):
            LeftTree = self.dfs(start, rootval-1)
            RightTree = self.dfs(rootval+1, end)
            for i in LeftTree:
                for j in RightTree:
                    root = TreeNode(rootval)
                    root.left = i
                    root.right = j
                    res.append(root)
        return res
    def generateTrees(self, n):
        if n==0: return []
        return self.dfs(1, n)


test = Solution()
# tn = TreeNode()
re = test.generateTrees(3)
for i in range(len(re)):
    pre_order(re[i])
    print('/n')

# pre_order(test.generateTrees(3)[1])
