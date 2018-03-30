def main():
	li = [int(i) for i in input().split(' ')]
	re = [0]*len(li)
	for i in range(len(li)):
		n = li[i]
		h = [0]*n
		h[0] = 3
		h[1] = 9
		if n>=3:
			for j in range(2,n):
				h[j] = 2*h[j-1] + h[j-2]
		re[i] = h[n-1]
	for i in range(len(li)):
		if i == len(li)-1:
			print(re[i], end='\n')
		else:
			print(re[i], end=' ')

if __name__ == '__main__':
	main()
