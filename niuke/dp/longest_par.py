"""
动态规划的核心在于找到最优子问题的结构和看是否有重复计算的子问题。此题中，
如果一个字串是最长的合法串，那么它一定能由另一个子串构造。从字符串s有后往前，
我们考虑s上的每一个位置，要是这个位置的字符包含在最长子串中，则我们可以由这个
子串的从第1个元素开始的子串的最大合法子串构造。换言之，dp[i]表示从s[i]到s[s.length - 1] 
包含s[i] 的最长的有效匹配括号子串长度，在s中从后往前，若s[i] == '('，则在s中从i开始
到s.length - 1计算dp[i]的值。在s中寻找从i + 1开始的有效括号匹配子串长度，即dp[i + 1]，
跳过这段有效的括号子串，查看下一个字符，其下标为j = i + 1 + dp[i + 1]。若j没有越界，
并且s[j] == ‘)’，则s[i ... j]为有效括号匹配，dp[i] =dp[i + 1] + 2。在求得了s[i ... j]的
有效匹配长度之后，若j + 1没有越界，则dp[i]的值还要加上从j + 1开始的最长有效匹配，即dp[j + 1]。
"""
class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        # print(n)
        dp = n*[0]
        Max = 0
        for i in range(n-2,-1,-1):
            print(i)
            if s[i] == '(':
                end = i+dp[i+1]+1
                if end >=n:
                    dp[i] = 0
                elif(s[end]==')'):
                    dp[i] = dp[i+1] + 2
                    if (end+1)<n:
                        dp[i]  = dp[i] + dp[end+1]
            Max = max(Max,dp[i])
        print(dp)
        return Max

s = Solution()

print(s.longestValidParentheses("()(()"))