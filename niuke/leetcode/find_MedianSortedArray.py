class Solution(object):
    def findMedianSortedArrays(self, a, b):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        c = a+b
        c.sort()
        m = int(len(c) / 2)
        mm = len(c) % 2
        # print(m,mm)
        if mm > 0 :
            return c[m]
        return (c[m-1]+c[m])/2.
        # if len1>len2:
        #     return self.findMedianSortedArrays(b,a)
        # if len1 ==0:
        #     if len2%2 > 0:
        #         return b[int(len2/2)]
        #     else:
        #         return (b[int(len2/2)-1]+b[int(len2/2)])/2.
        # len1 = len(a)
        # len2 = len(b)
        # k = len1+len2
        # p = min(max(k/2,1),len1)
        # q = k-p
test = Solution()
print(test.findMedianSortedArrays([1,2,5],[3,4]))