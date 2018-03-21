def main():
	[n,k] = [int(i) for i in input().split(' ')]
	li = [[0 for i in range(k+1)] for j in range(n+1)]
	for i in range(0,n+1):
		li[i][0] = 1
	for i in range(2,n+1):
		for j in range(1,i):
			if j<=k:
				if j==i-1:
					li[i][j]= 1
				else:
					li[i][j] = (li[i-1][j-1]*(i-j) + li[i-1][j]*(j+1))%2017
	print(li[n][k])

if __name__ == '__main__':
		main()	

