class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target<=nums[0]:
            return 0
        elif target>nums[-1]:
            return len(nums)
        elif target==nums[-1]:
            return len(nums)-1
        else:
            for i in range(1,len(nums)):
                if (nums[i-1]<=target)&(nums[i]>=target):
                    return i

test = Solution()
print(test.searchInsert([1,3,5,6],7))