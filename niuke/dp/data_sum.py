def main():
	[n,Sum] = [int(i) for i in input().split(',')]
	A = [int(i) for i in input().split(' ')]
	Li = [[0 for i in range(Sum+1)] for j in range(n+1)]
	for i in range(n+1):
		Li[i][0] = 1
	print(Li)
	for i in range(1,n+1):
		for j in range(1,Sum+1):
			if A[i-1] >j:
				Li[i][j] = Li[i-1][j]
			else:
				Li[i][j] = Li[i-1][j] + Li[i-1][j-A[i-1]]
	print(Li)

if __name__ == '__main__':
	main()