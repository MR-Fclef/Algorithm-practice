import numpy as np 


dnaList1 = [str(i) for i in input().split(' ')]
dnaList2 = [str(i) for i in input().split(' ')]

def peidui_dna(dnaList1,dnaList2):
	num = 0
	for i in range(len(dnaList1)):
		if dnaList1[i] == 'A':
			x = 'T'
			if x != dnaList2[i]:
				num = num+1
		elif dnaList1[i] == 'T':
			x = 'A'
			if x != dnaList2[i]:
				num = num+1
		elif dnaList1[i] == 'C':
			x = 'G'
			if x != dnaList2[i]:
				num = num+1
		elif dnaList1[i] == 'G':
			x = 'C'
			if x != dnaList2[i]:
				num = num+1
		else:
			print("DNA error...")
	return num

answer = peidui_dna(dnaList1,dnaList2)
print(answer)