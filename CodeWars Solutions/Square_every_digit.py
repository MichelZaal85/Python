# Welcome. In this kata, you are asked to square every digit of a number.
# For example, if we run 9119 through the function, 811181 will come out.
# Note: The function accepts an integer and returns an integer

def square_digits(num):
	s = []
	for i in str(num):
		s.append(str(int(i)**2)) # s += str(int(x)**2)
	return int(''.join(s))


# def square_digits(num):
#    return int(''.join(str(int(d)**2) for d in str(num)))