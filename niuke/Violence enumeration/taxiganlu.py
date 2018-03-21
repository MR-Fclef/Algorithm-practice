import numpy as np 

n = int(input())
taxi_XY = np.zeros((n,2))
for i in range(n):
	taxi_XY[i] = [x for x in input().split(' ')]
office_XY = [int(x) for x in input().split(' ')]
walktime = int(input())
taxitime = int(input())

near_taxiXY = np.zeros((1,2))
near_taxiXY[0,0] = taxi_XY[0,0]
near_taxiXY[0,1] = taxi_XY[0,1]

print(n)
print(taxi_XY)
print(office_XY)
print(walktime)
print(taxitime)

for x in range(n):
	taxilenth = abs(taxi_XY[x,0]) + abs(taxi_XY[x,1])
	if (abs(near_taxiXY[0,0]) + abs(near_taxiXY[0,1])) > taxilenth:
		near_taxiXY[0,0] = taxi_XY[x,0]
		near_taxiXY[0,1] = taxi_XY[x,1]
print(near_taxiXY)
if (abs(office_XY[0])+abs(office_XY[1]))*walktime < (abs(near_taxiXY[0,0])+abs(near_taxiXY[0,1]))*walktime+(abs(office_XY[0]-near_taxiXY[0,0])+abs(office_XY[1]-near_taxiXY[0,1]))*taxitime:
	print((abs(office_XY[0])+abs(office_XY[1]))*walktime)
else:
	print((abs(near_taxiXY[0,0])+abs(near_taxiXY[0,1]))*walktime+(abs(office_XY[0]-near_taxiXY[0,0])+abs(office_XY[1]-near_taxiXY[0,1]))*taxitime)