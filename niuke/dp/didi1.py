import sys
import math

class Solution:
    def dfs(self,arr,x,y,z,n,res):
        if len(arr)==n and arr not in res:
            res.append(arr)
        for i in range(n):
            if arr == []:
                self.dfs(arr+['A'],x-1,y,z,n-1,res)
                self.dfs(arr+['B'],x,y-1,z,n-1,res)
                self.dfs(arr+['C'],x,y,z-1,n-1,res)
            else:
                if arr[-1] == 'A':
                    if y>0:
                        self.dfs(arr+['B'],x,y-1,z,n-1,res)
                    if z>0:
                        self.dfs(arr+['C'],x,y,z-1,n-1,res)
                if arr[-1] == 'B':
                    if x>0:
                        self.dfs(arr+['A'],x-1,y,z,n-1,res)
                    if z>0:
                        self.dfs(arr+['C'],x,y,z-1,n-1,res)
                if arr[-1] == 'C':
                    if x>0:
                        self.dfs(arr+['A'],x-1,y,z,n-1,res)
                    if y>0:
                        self.dfs(arr+['B'],x,y-1,z,n-1,res)
    

inp = sys.stdin.readline().split(' ')
np = int(inp[0])
nq = int(inp[1])
nr = int(inp[2])
n = np+nq+nr
test = Solution()
res  =[]
test.dfs([],np,nq,nr,n,res)
print(len(res))



# test = Solution()
# test.dfs([],np,nq,nr,n)

      
                    
                    

