import numpy

# def duizuantou():
# 	n = int(input())
# 	height = [int(i) for i in input().split(' ')]
# 	s = sum(height)
# 	print(s)
# 	m = int(s/2)
# 	li = [[0 for i in range(m+1)] for j in range(n+1)]
# 	print(li)
# 	if m != (s-m):
# 		return -1
# 	else:
# 		for i in range(1,n+1):
# 			for j in range(1,m+1):
# 				if height[i-1] >j:
# 					li[i][j] = li[i-1][j]
# 				else:
# 					li[i][j] = max(li[i-1][j],li[i-1][j-height[i-1]]+height[i-1])
# 				if li[i][j] >500000:
# 					return -1
# 	if li[n][m] <= (s-m):
# 		return li[n][m]
# 	else:
# 		return -1
def main(n,sum1,sum2):
	global ans
	if sum1 == sum2:
		ans = max(ans,sum1)
	if n==0:
		return
	if sum1>MAX:
		return
	if (sum1+summ[n-1])<sum2:
		return
	if ((sum1+sum2+summ[n-1])<=ans*2):
		return
	main(n-1,min(sum1+height[n-1],sum2),max(sum1+height[n-1],sum2))
	main(n-1,min(sum2+height[n-1],sum1),max(sum2+height[n-1],sum1))
	main(n-1,sum1,sum2)

if __name__ == '__main__':
	n = int(input())
	height_shuru = [int(i) for i in input().split(' ')]
	height = sorted(height_shuru)
	summ = [0]*n
	summ[0] = height[0]
	MAX = 500000
	ans = 0
	for i in range(1,n):
		summ[i] = summ[i-1]+height[i]
	main(n,0,0)
	if ans != 0:
		print(ans)
	else:
		print(-1)