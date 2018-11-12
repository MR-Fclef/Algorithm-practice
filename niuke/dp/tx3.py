import sys
import math
k = sys.stdin.readline().split(' ')
x = int(k[0])
y = int(k[1])
z = int(k[2])
count = 0
arr = []
for i in range(1,x+1):
    arr.append(i)
    for j in range(1,y+1):
        arr.append(j)
        for m in range(1,z+1):
            arr.append(m)
            arr.sort()
            if arr[0]+arr[1]>arr[2]:
                print(arr)
                count += 1
                arr.remove(m)
            else:
                arr.remove(m)
        arr.remove(j)
    arr.remove(i)
print(count)

