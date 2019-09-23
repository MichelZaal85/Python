n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here

def flatten(x):
    results = []
    for numbers in x:
        for i in numbers:
            results.append(i)
    return results


print (flatten(n))

# from itertools import chain
# def flatten_and_sort(array):
# 	return sorted((chain(*array)))