def get_sum(a,b):
	if a == b:
		return a or b
	if a < 0 and b < 0:
		return 0
	if a < 0:
		return b
	if b < 0:
		return a

	return a + b


# Given two integers a and b, which can be positive or negative, find the sum of all the numbers between including 
# them too and return it. If the two numbers are equal return a or b.
# Note: a and b are not ordered!

# get_sum(1, 0) == 1   // 1 + 0 = 1
# get_sum(1, 2) == 3   // 1 + 2 = 3
# get_sum(0, 1) == 1   // 0 + 1 = 1
# get_sum(1, 1) == 1   // 1 Since both are same
# get_sum(-1, 0) == -1 // -1 + 0 = -1
# get_sum(-1, 2) == 2  // -1 + 0 + 1 + 2 = 2