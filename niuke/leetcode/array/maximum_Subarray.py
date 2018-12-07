class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        Max = nums[0]
        Sum = 0
        n = len(nums)
        for i in range(n):
            Sum = nums[i]+Sum
            if Sum >=0:
                if Sum > Max:
                    Max = Sum
            else:
                if Sum >Max:
                    Max = Sum
                    Sum = 0
                Sum = 0
        return Max