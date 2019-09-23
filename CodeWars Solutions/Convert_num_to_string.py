def num_to_str(num):
	return str(num)

# equal
number_to_string = str

# str is already a reserved keyword which is in-fact a function,
# therefore you can pass it arguments. it's making number_to_string equal to the str function. 

# This method is technically the same as the str function and any 
# arguments that are passed to number_to_string are passed through the 
# str function. 

# There is no point having a function within a function (an embedded function), 
# so you can access the function directly by simply stating it rather than 
# wrapping it up in a lambda or a def function.

number_to_string = lambda x: (str)
