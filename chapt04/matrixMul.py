from numpy import *  

# Here，i make a mistake called index 1 is out of bounds for axis 0 with size 1
# It costs me much time to deal with: res = mat(zeros((n,n))) res[i][j]
# the two codes is the reason why the compiler told me the error
# zeros() function generate a array like [[..],[..],[..]] and we can decribe the value by res[i][j]
# mat(zeros()) will generate a martrix and res[i] is still a martrix, so we only use res[i,j] to represent the value.
# List array matrix set**


def matrixMul(A,B):
	n = max(shape(A))
	res = zeros((n,n))
	print res
	for i in range(len(A)):
		for j in range(len(B[0])):
			for k in range(len(B)):
				res[i][j] += A[i][k] * B[k][j]
	return mat(res)

if __name__== "__main__": 
	a = [[1,2], [3,4], [5,6], [7,8]]
	b = [[1,2,3,4], [5,6,7,8]]
	aa = matrixMul(a,b)
	print aa
	print aa[1,2]
	# n = max(shape(a))
	# for i in range(len(a)):
	# 	print i
	# for j in range(len(b[0])):
	# 	print j
	# for k in range(len(b)):
	# 	print k
	# res = zeros((n,n))
	# #res[1][2] = a[1][1]*b[1][2]
	# print res[0][0]
	# print a[0][0]
	# print res
	# print mat(a)

