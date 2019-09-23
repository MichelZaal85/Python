# Compute the number of feet corresponding to a number of miles.

###################################################
# Miles to feet conversion formula
# Student should enter function on the next lines.

# There are 5280 feet in a mile. Write a Python statement that calculates and prints the number of feet in 13 miles.


def miles_to_feet(miles):
    return miles * 5280


###################################################
# Tests
# Student should not change this code.

def test(miles):
	print(str(miles) + " miles equals" str(miles_to_feet(miles)) + " feet.")

test(13)
test(57)
test(82.67)


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#13 miles equals 68640 feet.
#57 miles equals 300960 feet.
#82.67 miles equals 436497.6 feet.
