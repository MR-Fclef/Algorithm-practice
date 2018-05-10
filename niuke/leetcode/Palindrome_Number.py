class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        n = len(x)
        start = 0
        end = n-1
        while start < end:
            if x[start] != x[end]:
                return False
            else:
                start = start + 1
                end = end - 1
        return True

test = Solution()
print(test.isPalindrome(123))