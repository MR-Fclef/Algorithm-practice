class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        self.res = []
        self.DFS(candidates,target,0,[])
        return self.res
    def DFS(self,candidates,target,start,valuelist):
        n = len(candidates)
        if target==0 and valuelist not in self.res:
            self.res.append(valuelist)
        for i in range(start,n):
            if candidates[i]>target:
                return
            else:
                self.DFS(candidates,target-candidates[i],i+1,valuelist+[candidates[i]])

test = Solution()
candidates = [10,1,2,7,6,1,5]
target = 8
print(test.combinationSum2(candidates,target))
