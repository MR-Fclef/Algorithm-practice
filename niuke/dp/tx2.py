import sys
import math
k = sys.stdin.readline().split(' ')
x = int(k[0])
y = int(k[1])
N = int((math.sqrt(1+8*(x+y))-1)/2)
print(N)
arr = [int(i) for i in range(1,N+1)]
print(arr)
count = 1
if x<=N:
    print(1)
else:
    for i in range(N):
        if (x-(N-i))>N-i-1:
            x = x-(N-i)
            count += 1
        else:      
            break
print(count+1)
            
        





