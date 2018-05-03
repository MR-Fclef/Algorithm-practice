def quick_sort(array,l,r):
	if l<r:
		q = partition(array,l,r)
		quick_sort(array,l,q-1)
		quick_sort(array,q+1,r)
	# print(array)
	return array

def partition(array,l,r):
	x= array[r]
	i = l-1
	for j in range(l,r):
		if array[j] <= x:
			i += 1
			array[i],array[j] = array[j],array[i]
	array[i+1],array[r] = array[r],array[i+1]
	print(i+1)
	return i+1
if __name__ == '__main__':
	s = [3,6,5,8,9,4,7，10]
	print(quick_sort(s,l=0,r = len(s)-1))