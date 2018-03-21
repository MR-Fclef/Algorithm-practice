import numpy as np 

def function(M,N):
	return len([i for i in set(N) if i in M])
if __name__ == '__main__':
	[n,m] = [int(x) for x in input().split(' ')]
	N = [x for x in input().split(' ')]
	M = [x for x in input().split(' ')]
	print(function(M,N))
