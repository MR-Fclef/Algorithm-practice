class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        Max = nums[0] 
        length = len(nums)  
        dp_min = [0]*length 
        dp_max = [0]*length  
        dp_min[0] = nums[0]
        dp_max[0] = nums[0]
        for i in range(1,length):
            dp_min[i] = min(min(dp_max[i - 1] * nums[i], dp_min[i - 1] * nums[i]), nums[i])
            dp_max[i] = max(max(dp_max[i - 1] * nums[i], dp_min[i - 1] * nums[i]), nums[i])
            Max = max(dp_max[i],Max) 
        return Max 
if __name__ == '__main__':
    gri = [2,3,-2,4]
    test = Solution()
    print(test.maxProduct(gri))