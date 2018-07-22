# class Solution:
#     def sortColors(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: void Do not return anything, modify nums in-place instead.
#         """
#         red_n = 0
#         white_n = 0
#         blue_n = 0
#         n = len(nums)
#         for i in range(n):
#             if nums[i]==0:
#                 red_n += 1
#             elif nums[i]==1:
#                 white_n += 1
#             elif nums[i]==2:
#                 blue_n += 1
#         for i in range(red_n):
#             nums[i] = 0
#         for i in range(white_n):
#             nums[red_n + i] = 1
#         for i in range(blue_n):
#             nums[red_n+white_n+i] = 2
class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums == []: return 
        p0 = 0; p2 = len(nums) - 1; i = 0
        while i <= p2:
            if nums[i] == 2:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1
            elif nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                p0 += 1
                i += 1
            else:
                i += 1
        