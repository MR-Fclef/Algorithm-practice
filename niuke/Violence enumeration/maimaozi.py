import numpy as np 

def function():
	n = int(input())
	li = [int(x) for x in input().split(' ')]
	print(li)
	if len(li) != n:
		print(0)
	elif len(set(li))<3:
		print(-1)
	else:
		s = sorted(set(li))
		print(s[2])

if __name__ == '__main__':
	function()

