import numpy as np

def function():
	l = [int(i) for i in input().split(' ')]
	sorted_l = sorted(l)
	count = 0
	x = 0
	for i in range(len(l)):
		if l[i] == sorted_l[x]:
			count = count + 1
			x = x+1
	return len(l)-count
if __name__ == '__main__':
	c = function()
	print(c)