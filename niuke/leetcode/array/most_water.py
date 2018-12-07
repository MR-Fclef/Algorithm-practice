class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        l = 0
        r = n-1
        Max = 0
        s = 0
        while l < r:
            if height[l]<height[r]:
                s = (r-l)*height[l]
                Max = max(s,Max)
                l = l + 1
            else:
                s = (r-l)*height[r]
                Max = max(s,Max)
                r = r - 1
        return Max
test = Solution()
print test.maxArea([1,2,4,3])

