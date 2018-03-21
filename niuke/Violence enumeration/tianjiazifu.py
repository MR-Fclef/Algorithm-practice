import numpy as np 

def tianjiazifu(x):
	A = [i for i in input().split(' ')]
	B = [i for i in input().split(' ')]
	count = 0
	if len(A)<len(B):
		for i in range(len(A)):
			if A[i] != B[i]:
				count = count+1
	elif len(A)==len(B):
		for j in range(len(B)):
			if B[j] != A[j]:
				count = count+1
	else:
		return -1
	return count

if __name__ == '__main__':
	a='e'
	print(tianjiazifu(a))