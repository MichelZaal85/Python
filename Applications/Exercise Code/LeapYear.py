'''
	Every year that is exactly divisible by four is a leap year, 
	except for years that are exactly divisible by 100, but these 
	centurial years are leap years if they are exactly divisible 
	by 400. For example, the years 1700, 1800, and 1900 are not 
	leap years, but the year 2000 is.
'''

# Compute whether the given year is a leap year.

###################################################
# Is leapyear formula
# Student should enter function on the next lines.

def is_leap_year(year):
	if year % 100 != 0 or year % 400 == 0:
		if year % 4 == 0:
			return True
	return False

###################################################
# Tests
# Student should not change this code.

def test(year):
	"""Tests the is_leapyear function."""
	if is_leap_year(year):
		print(year, "is a leap year.")
	else:
		print(year, "is not a leap year.")

test(2000)
test(1996)
test(1800)
test(2013)

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#2000 is a leap year.
#1996 is a leap year.
#1800 is not a leap year.
#2013 is not a leap year.
