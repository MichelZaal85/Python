def sum_str(a,b):
	if a and b:
		return str(int(a) + int(b))
	elif a or b:
		return a or b
	return str(0)
	

print(sum_str('1985','32'))

print(sum_str('1985',''))
print(sum_str('','32'))

print(sum_str('',''))

# example:

# def sum_str(a, b):
#     return str(int(a or 0) + int(b or 0))