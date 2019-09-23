# Printing "Goodbye" with a global message variable

###################################################
# Student should enter function on the next lines.


# Define globals - Constants are capitalized in Python
HEIGHT = 400
WIDTH = 400
RADIUS_INCREMENT = 5
ball_radius = 20

def set_goodbye():
    global message
    message = 'Goodbye'

###################################################
# Tests

message = "Hello"
print message
set_goodbye()
print message

message = "Ciao"
print message
set_goodbye()
print message


###################################################
# Output

#Hello
#Goodbye
#Goodbye
#Ciao
#Goodbye
#Goodbye



# Functions to manipulate global variable count

###################################################
# Student should enter function on the next lines.
count = 0
# Reset global count to zero.
def reset():
    global count
    count = 0

# Increment global count.
def increment():
    global count
    count += 1

# Decrement global count.
def decrement():
    global count
    count -= 1

# Print global count.
def print_count():
    print(count)





point = [0,0]

# Whenether you don't change to full global variable, You don't need to 
# set is a global in the function.
def function1():
	point[0] += 1
	point[1] += 2


# This will create an error, because we're trying to alter the full variable, 
# instead of a part. 

def function2():
	point[50,50]
###################################################
# Test

# note that the GLOBAL count is defined inside a function
reset()		
increment()
print_count()
increment()
print_count()
reset()
decrement()
decrement()
print_count()

####################################################
# Output
#1
#2
#-2