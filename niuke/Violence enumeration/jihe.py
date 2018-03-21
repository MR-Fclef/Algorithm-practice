import numpy as np 

def getNum(w,x,y,z):
	l = []
	for i in range(w,x+1):
		for j in range(y,z+1):
			s = float(i)/j
			l.append(s)
	print(l)
	return len(set(l))

if __name__ == '__main__':
	[w,x,y,z] = [int(x) for x in input().split(' ')]
	print(getNum(w,x,y,z))