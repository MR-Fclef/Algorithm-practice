class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        self.res = []
        n = len(nums)
        self.dfs(n,nums,[])
        return self.res
    def dfs(self,n,nums,valuelist):
        if valuelist not in self.res:
            
            self.res.append(valuelist)
        
        for i in range(n):
            
            self.dfs(n-i-1,nums[i+1:],valuelist+[nums[i]])