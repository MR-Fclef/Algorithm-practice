import numpy as np 


def shuzubianhuan():
	s = [int(i) for i in input().split(' ')]
	if len(set(s)) == 1:
		print("YES")
	else:
		for i in range(len(s)):
			while ((s[i]%2)!=1):
				s[i] = int(s[i]/2)
		if len(set(s))==1:
			print("YES")
		else:
			print("NO")
if __name__ == '__main__':
	shuzubianhuan()