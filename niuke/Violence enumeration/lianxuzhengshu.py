import numpy as np 

n = int(input())
zhengshu = [int(i) for i in input().split(' ')]
# print(zhengshu)
# print(len(zhengshu))
def lianxuzhegshu(n,zhengshu):
	x = 0
	l = sorted(zhengshu)
	# print(l[0]-1)
	if len(set(l)) < n:
		print('mistake...')
		return;
	for i in range(len(l)-1):
		if l[i] != l[i+1]-1:
			print(l[i]+1)
		else:
			x = x+1
	if x == n-1:
		print(l[0]-1,l[-1]+1)

lianxuzhegshu(n,zhengshu)
