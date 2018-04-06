class Solution:
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m = len(t)+1
        n = len(s)+1
        dp = [[0 for j in range(n)] for i in range(m)]
        for i in range(1,m):
            dp[i][0] = 0
        for j in range(n):
            dp[0][j] = 1
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i][j-1] + (dp[i-1][j-1] if s[j-1]==t[i-1] else 0 )
        return dp[m-1][n-1]
s = Solution()

print(s.numDistinct("bird","ibdr"))