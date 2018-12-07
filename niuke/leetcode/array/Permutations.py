# class Solution:
#     def permute(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         nums.sort()
#         self.n = len(nums)
#         self.res = []
#         self.DFS(nums,0,[])
#         return self.res
#     def DFS(self,nums,start,valuelist):
#         # print(nums,start,valuelist)
#         if start == self.n:
#             print(valuelist[0])
#             self.res.append(valuelist[:])
#         for i in nums:
#             if i in valuelist:
#                 continue
#             valuelist.append(i)
#             self.DFS(nums,start+1,valuelist)
#             valuelist.remove(i)

# class Solution:
#     # @param num, a list of integer
#     # @return a list of lists of integers
#     def permute(self, num):
#         if len(num) == 0: return []
#         if len(num) == 1: return [num]
#         res = []
#         for i in range(len(num)):
#             for j in self.permute(num[:i] + num[i+1:]):
#                 print(j)
#                 res.append([num[i]] + j)
#                 print(res)
#         return res

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        if len(num) == 0: return []
        if len(num) == 1: return [num]
        self.n = len(num)
        self.res = []
        self.dfs(num,[])
        return self.res
    def dfs(self,num,valuelist):
        if len(valuelist)==self.n:
            self.res.append(valuelist)
        for i in range(len(num)):
            self.dfs(num[:i]+num[i+1:],valuelist+[num[i]])


test = Solution()
nums =[1,2,3]
re = test.permute(nums)
print(re)