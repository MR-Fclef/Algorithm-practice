class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        def dfs(depth, start, valuelist):
            res.append(valuelist)
            if depth == n: return
            for i in range(start, n):
                dfs(depth+1, i+1, valuelist+[nums[i]])
        #nums.sort()
        res = []
        dfs(0, 0, [])
        return res



test = Solution()
print(test.subsets([1,2,3]))