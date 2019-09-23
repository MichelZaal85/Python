def g(a,b):
	
	# if a == True and b == False:
	# 	return True
	# else:
	# 	return False
	
	# shorthand notation for above 
	return a and not(b)

print(g(True, True))	# False
print(g(True, False))	# True
print(g(False, True))	# False
print(g(False, False))	# False