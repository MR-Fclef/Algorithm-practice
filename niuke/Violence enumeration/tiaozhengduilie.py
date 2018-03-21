import numpy as np 

duilie = [x for x in input().split(' ')]
g = 0
b = 0
sum_g = 0
sum_b=0
for x in range(len(duilie)):
	if duilie[x] == 'G':
		g = g+1
		sum_g = sum_g + x
	else:
		b = b+1
		sum_b = sum_b + x
boy_tiaozheng = sum_b - b*(b - 1)/2
girl_tiaozheng = sum_g - g*(g - 1)/2
if boy_tiaozheng<=girl_tiaozheng:
	print(boy_tiaozheng)
else:
	print(girl_tiaozheng)