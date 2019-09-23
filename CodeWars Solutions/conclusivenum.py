def first_non_consecutive(arr):
	for i in range(0, len(arr)-1):
		if arr[i+1] - arr[i] != 1:
			return arr[i+1]
	return "Null"
print(first_non_consecutive([1,2,3,4,5,7,8,10,11,12,13]))

# def first_non_consecutive(arr):
#     return next((j for i, j in zip(arr, arr[1:]) if i + 1 != j), None)