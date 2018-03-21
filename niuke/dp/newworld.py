#DP Algorithm : 学习01背包问题
#学习下来感觉和最长公共子序列的思路很类似，毕竟都是DP思想！
import numpy as np 
def createWorld():
	x,n,m = [int(i) for i in input().split(' ')]
	zeros = [0]*x
	ones = [0]*x
	for i in range(x):
		item = input()
		zeros[i],ones[i] = count01(item)

	li = [[0 for i in range(m+1)] for j in range(n+1)]
	for i in range(1,x+1):
		for j in range(n,zeros[i-1]-1,-1):
			for t in range(m,ones[i-1]-1,-1):
				li[j][t] = max(li[j][t],1+li[j-zeros[i-1][t-ones[i-1]]])
	print(li[n][m])

def count01(item):
	c = 0
	for i in item:
		if int(i) == 1:
			c = c+1
	return len(item)-c,c

if __name__ == '__main__':
	createWorld()
