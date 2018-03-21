#分饼干这一题有点问题；还有01反转；还有优美的回文串
import numpy as np 

def function(l,n):
	x_weizhi = []
	k=0
	count = 0
	for x in range(len(l)):
		if l[x] == 'x':
			x_weizhi.append(x)
			l[x] = 0
	print(x_weizhi)
	for i in range(len(x_weizhi)):
		for j in range(10):
			l[x_weizhi[i]] = j
			for m in range(len(l)):
				k = int(l[m])*(10^(len(l)-m)) + k
			if float(k)%n == 0:
				count = count+1
				print(k)
	return count	
if __name__ == '__main__':
	l = [x for x in input()]
	n = int(input())
	count = function(l,n)
	print(count)