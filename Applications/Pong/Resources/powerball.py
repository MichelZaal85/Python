'''
Write a Python function powerball that takes no arguments and prints the message 
"Today's numbers are %, %, %, %, and %. The Powerball number is %.". 

The first five numbers should be random integers in the range (1,60), 
i.e., at least 1, but less than 60. In reality, these five numbers must all be distinct, but for 
this problem, we will allow duplicates. 

The Powerball number is a random integer in the range (1,36), 
i.e., at least 1 but less than 36. 

Use the random module and the function random.randrange() to generate the appropriate random numbers.
Note that this function should print the desired message, rather than returning it as a string.
'''

# Compute and print powerball numbers.

###################################################
# Powerball function
# Student should enter function on the next lines.
import random
def powerball():
	lotnumber = set()
	while len(lotnumber) < 6:
		lotnumber.add(random.randint(1,60))
	lotnumber = list(lotnumber)
	powerball = random.randint(1,30)
	print("Today's numbers are %d, %d, %d, %d, and %d. The Powerball number is %d." %(lotnumber[0], lotnumber[1], lotnumber[2],lotnumber[3],lotnumber[4], powerball))
	
###################################################
# Tests
# Student should not change this code.
	
powerball()
powerball()
powerball()
