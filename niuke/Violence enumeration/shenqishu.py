import numpy as np 

def isZhishu(x):
	for i in range(2,x):
		if x%i == 0:
			return False
	return True
def isShenjingshu(x):
	for i in x:
		m1 = x
		m1.remove(i)
		for j in m1:
			new_data = i*10 + j
			if isZhishu(new_data):
				print(new_data)
				return True
			else:
				continue
	return False
def data_fenge(x):
	fenge = []
	while (x>0):
		if (x%10)!=0:
			fenge.append(x%10)
		x = int(x/10)		
	return fenge
def num_zhishu():
	ab = [int(i) for i in input().split(' ')]
	a = ab[0]
	b = ab[1]
	count = 0
	for x in range(a,b+1):
		if x>10:
			print(x)
			fenge = data_fenge(x)
			print(fenge)
			if isShenjingshu(fenge):
				count = count+1
	return count

if __name__ == '__main__':
	c = num_zhishu()
	print(c)