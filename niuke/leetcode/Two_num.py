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
    def Testsum(self,nums,target):
    	ddict = {}
    	for i in range(len(nums)):
    		x = nums[i]
    		if target-x in ddict:
    			return (ddict[target-x],i)
    		ddict[x] = i
    	print(ddict)
if __name__ == '__main__':
	nums = [1,2,7,9,11,15]
	target = 9
	test = Solution()
	print(test.Testsum(nums,target))