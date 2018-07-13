# class Solution:
#     def permuteUnique(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         if len(nums) == 0: return []
#         if len(nums) == 1: return [nums]
#         self.n = len(nums)
#         self.res = []
#         self.dfs(nums,[])
#         return self.res
#     def dfs(self,nums,valuelist):
#         if len(valuelist)==self.n and valuelist not in self.res:
#             self.res.append(valuelist)
#         for i in range(len(nums)):
#             self.dfs(nums[:i]+nums[i+1:],valuelist+[nums[i]])


class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0: return []
        if len(nums) == 1: return [nums]
        self.n = len(nums)
        self.res = []
        self.dfs(nums,[])
        return self.res
    def dfs(self,nums,valuelist):
        if len(valuelist)==self.n:
            self.res.append(valuelist)
        for i in range(len(nums)):
            if nums[i] in nums[:i]:
                continue
            self.dfs(nums[:i]+nums[i+1:],valuelist+[nums[i]])