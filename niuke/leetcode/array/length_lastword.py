class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        arr = s.split(' ')
        n = len(arr)
        i = 0
        while(len(arr[-1-i])==0):
            if (i + 1) == n:
                return 0
            i = i+1
                
        return len(arr[-1-i])

test = Solution()
test.lengthOfLastWord(" ")