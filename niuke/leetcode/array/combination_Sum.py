class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        self.res = []
        self.DFS(candidates, target, 0, [])
        return self.res
    def DFS(self, candidates, target, start, valuelist):
        n = len(candidates)
        if target==0:
            return self.res.append(valuelist)
        for i in range(start,n):
            if candidates[i]>target:
                return
            self.DFS(candidates, target - candidates[i], i, valuelist + [candidates[i]])