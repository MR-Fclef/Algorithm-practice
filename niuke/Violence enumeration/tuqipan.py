import numpy as np 

def function(n,l):
	s = 1
	s_max = 0
	for j in range(n):
		for i in range(n-1):
			if l[i] == l[i+1]:
				s = s+1
				s_max = max(s_max,s)
			else:
				s = 1
	return s_max
if __name__ == '__main__':
	n = int(input())
	l = []
	for x in range(n):
		l.append(input())
	s_max = function(n,l)
	print(s_max)