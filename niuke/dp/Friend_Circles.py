class Solution:
	def findCircleNum(self, M):
		global m 
		m = len(M)
		if m ==0:
			return 0
		flag = [0]*m
		cirle = 0
		for i in range(m):
			if flag[i] == 0:
				Solution.mark(M,flag,i)
				cirle = cirle + 1
		return cirle
	def mark(M,flag,k):
		flag[k] = 1
		for i in range(m):
			if (flag[i]==0)&(M[k][i]==1):
				Solution.mark(M,flag,i)

s = Solution()
M = [[1,1,0],[1,1,0],[0,0,1]]
print(s.findCircleNum(M))