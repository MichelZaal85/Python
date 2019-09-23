def to_alternating_case(string):
	converted_string = []
	for c in string:
		if c.isupper():
			converted_string.append(c.replace(c, c.lower()))
		else:
			converted_string.append(c.replace(c, c.upper()))
	return "".join(converted_string)
print(to_alternating_case("MichEl"))


# def to_alternating_case(string):
#	return string.swapcase()