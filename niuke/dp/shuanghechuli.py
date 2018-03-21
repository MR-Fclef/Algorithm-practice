import numpy

def main():
	n = int(input())
	data_n = [i for i in input().split(' ')]
	time = []
	sum_time = 0
	for i in range(n):
		sum_time = sum_timem + data_n[i]/1024
		time.append(data_n[i]/1024)
	max_time = int(sum_time/2)
	li = [[0 for i in range(n+1)] for j in range(max_time+1)]
	for i in range(1,n+1):
		for j in range(1,max_time+1):
			if j<time[i-1]:
				li[i][j] = li[i-1][j]
			else:
				li[i][j] = max(li[i-1][j],li[i-1][j-time[i-1]]+time[i-1])
	return li[n][max_time]
if __name__ == '__main__':
	main()
	
