import numpy as np 

n = int(input())
li =np.zeros((n,2))

for i in range(n):
	li[i] = [x for x in input().split(' ')]
# print(li[:,0])
x_min = min(li[:,0])
x_max = max(li[:,0])
y_min = min(li[:,1])
y_max = max(li[:,1])
rectangle_s = (x_max - x_min) * (y_max - y_min) 
print(rectangle_s)
# def function(li):



	