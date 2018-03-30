import numpy

def main():
	n = int(input())
	d = [0]*n
	j=0
	for i in range(n):
		d[i] = int(input())
	for i in range(n):
		if d[i] != 0:
			d[j] = d[i]
			j = j+1
	for i in range(j,n):
		d[i] = 0
	for i in range(n):
		print(d[i])
if __name__ == '__main__':
	main()
