import numpy as np 

# fishsize_list = [i for i in range(1,11)]
# minSize = 11
# maxSize = 120
# n = len(fishsize_list)
# print(fishsize_list)
# print(n)


# def fish(fishsize_list,minSize,maxSize):
# 	for i in range(minSize,maxSize+1):
# 		print(i)
# 		n = len(fishsize_list)
# 		x = 0
# 		t1 = float(i*2)
# 		t2 = float(i*10)
# 		# print(t3)
# 		for j in range(n):
# 			print(j)
# 			if ((fishsize_list[j] <= t2) and (fishsize_list[j] >= t1))or ((i <= fishsize_list[j]*10) and (i >= fishsize_list[j]*2)):
# 				break
# 			else:
# 				x = x+1
# 				print(x)
# 		if x == n:
# 			fishsize_list.append(i)
# 	return fishsize_list

# newfish = fish(fishsize_list,minSize,maxSize)
# print(newfish)


[minSize,maxSize] = [int(i) for i in input().split(' ')]
n = input()
fishSize = [int(i) for i in input().split(' ')]
okLis = fishSize

for newSize in range(minSize,maxSize+1):
	ok = True
	for oldSize in fishSize:
		if oldSize<=newSize*10 and oldSize>=newSize*2:
			ok = False
			break
		if newSize<=oldSize*10 and newSize>= oldSize*2:
			ok = False
			break
	if ok == True:
		okLis.append(newSize)
print(okLis)