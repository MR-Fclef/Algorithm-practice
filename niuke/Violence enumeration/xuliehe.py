import numpy as np 
[N,L] = [int(i) for i in input().split(' ')]
def xuliehe(N,L):
	for a1 in range(int(N/2),0,-1):
		for n in range(L,int(N/2)):
			if (n*a1+n*(n-1)/2) == 18:
				for j in range(n):
					print(a1+j)
				return;
			elif (n*a1+n*(n-1)/2) > 18:
				break
			else:
				continue
xuliehe(N,L)