class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.res = []
        
        self.dfs(1,n,k,[])
        
        return self.res
    def dfs(self,a1,a2,b,c):
        if b == 0:
            self.res.append(c)
        if a1 <= a2:

            for i in range(a1,a2+1):
                self.dfs(i+1,a2,b-1,c+[i])
        else:
            return

test = Solution()
print(test.combine(4,2))