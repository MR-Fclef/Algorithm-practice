class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        index=0
        reach=0
        if len(nums)<=1:
            return True
        while index<len(nums):
            if reach<index:
                return False
            reach=max(reach,nums[index]+index)
            index+=1
        return True
test = Solution()
print(test.canJump([2,3,1,1,4]))