# String list joining problem

###################################################
# Student should enter code below
'''
Write a function string_list_join(string_list) that takes a list of strings 
as input and returns a single string that is the concatenation of the lists 
in the string. We recommend using a for loop to implement this function.
'''
def string_list_join(l):
	temp = []
	for i in l:
		temp.append(i)
	return str(temp)

###################################################
# Test data

print(string_list_join([]))
print(string_list_join(["pig", "dog"]))
print(string_list_join(["spam", " and ", "eggs"]))
print(string_list_join(["a", "b", "c", "d"]))


###################################################
# Output

#
#pigdog
#spam and eggs
#abcd