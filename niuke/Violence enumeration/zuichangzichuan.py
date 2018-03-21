import numpy as np 

X = [i for i in input().split(' ')]
Y = [i for i in input().split(' ')]

def LCS_Length(X,Y):
	m = len(X)
	n = len(Y)
	b =np.zeros((m,n))
	c =np.zeros((m+1,n+1))
	# for i in range(0,m):
	# 	c[i,0] = 0
	# for j in range(0,m):
	# 	c[0,j] = 0
	for i in range(1,m+1):
		for j in range(1,n+1):
			if X[i-1] == Y[j-1]:
				c[i,j] = c[i-1,j-1] + 1
				# b[i,j] = 'left_up'
			elif c[i-1,j] >= c[i,j-1]:
				c[i,j] = c[i-1,j]
				# b[i,j] = 'up'
			else:
				c[i,j] = c[i,j-1]
				# b[i,j] = 'left'
	return c

def LCS_lianxu(X,Y):
	m = len(X)
	n = len(Y)
	b =np.zeros((m,n))
	c =np.zeros((m+1,n+1))
	for i in range(1,m+1):
		for j in range(1,n+1):
			if X[i-1] == Y[j-1]:
				c[i,j] = c[i-1,j-1] + 1
				# b[i,j] = 'left_up'
			else:
				c[i,j] = 0
				# b[i,j] = 'left'
	return c

c1 = LCS_Length(X,Y)
print(c1)

c2 = LCS_lianxu(X,Y)
print(c2)