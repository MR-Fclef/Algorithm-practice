import numpy as np 

def yematongji():
	n = int(input())
	num_count = [0]*10
	for x in range(1,n+1):
		while (x>0):
			t = x%10
			x = int(x/10)
			num_count[t] = num_count[t] + 1
	print(num_count)

if __name__ == '__main__':
	yematongji()