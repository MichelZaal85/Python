# return the indexnumber of the middle element number of an array of 3

def gimme(input_array):
	L = input_array.copy()
	input_array.sort()
	return L.index(input_array[1])



# Examples:

# Shorter version example:
def gimme(inputArray):
    # Implement this function
    return inputArray.index(sorted(inputArray)[1])


# Very short example
gimme=lambda l:l.index(sorted(l)[1])


def gimme(lst):
    return lst.index(sorted(lst)[len(lst)//2])