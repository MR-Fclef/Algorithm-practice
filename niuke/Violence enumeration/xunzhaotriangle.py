import numpy as np 
import math


def L(x,y):
	return math.sqrt(math.pow((float(x[1])-float(y[1])),2)+math.pow((float(x[2])-float(y[2])),2)+math.pow((float(x[3])-float(y[3])),2))

def S(a,b,c):
	p = (a+b+c)/2
	return math.sqrt(p*(p-a)*(p-b)*(p-c))

def isSan(a,b,c):
	if(a<(b+c)) & (b<(a+c)) & (c<(a+b)):
		return True
	else:
		return False

def isColor(x,y,z):
	if (x[0]==y[0]) & (x[0]==z[0]):
		return True
	elif (x[0]!=y[0])&(x[0]!=z[0])&(y[0]!=z[0]):
		return True
	else:
		return False

def s_Max():
	n = int(input())
	N = np.zeros((n,4))
	M =[]
	s_max = 0
	for i in range(n):
		M.append([str(j) for j in N[i]])
		M[i] = [x for x in input().split(' ')]
	print(M)
	for i in range(n-2):
		for j in range(i+1,n-1):
			for m in range(j+1,n):
				print(L(M[i],M[j]))
				print(L(M[i],M[m]))
				print(L(M[j],M[m]))
				print(isSan(L(M[i],M[j]),L(M[i],M[m]),L(M[j],M[m])))
				if isSan(L(M[i],M[j]),L(M[i],M[m]),L(M[j],M[m])) & isColor(M[i],M[j],M[m]):
					s_max = max(s_max,S(L(M[i],M[j]),L(M[i],M[m]),L(M[j],M[m])))
	return s_max

if __name__ == '__main__':
	print(s_Max())

		
