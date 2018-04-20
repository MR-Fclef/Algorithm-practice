class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        for i in range(len(nums)-1):
        	for j in range(i+1,len(nums)):
        		if (nums[i] + nums[j]) == target:
        			result.append(i)
        			result.append(j)
        return result

if __name__ == '__main__':
	nums = [3,2,4]
	target = 6
	test = Solution()
	print(test.twoSum(nums,target))