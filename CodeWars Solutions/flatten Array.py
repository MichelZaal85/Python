def flatten_and_sort(array):
	l = []
	for i in array:
		for n in i:
			l.append(n)
	l.sort()
	return l
print(flatten_and_sort([[4,5,6],[1,2,3],[9,8,7]]))


from itertools import chain
def flatten_and_sort(array):
	return sorted((chain(*array)))