class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        res = [[1 for i in range(n)] for j in range(m)]
        if m == 1:
            return 1
        if n == 1:
            return 1
        for i in range(1,m):
            for j in range(1,n):
                res[i][j] = res[i-1][j] + res[i][j-1]
        return res[m-1][n-1]