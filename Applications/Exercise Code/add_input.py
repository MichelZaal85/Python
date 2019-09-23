# Echo an input field

###################################################
# Student should add code where relevant to the following.

import simplegui 

# Handlers for input field
    
# add_input, gives get_input the input it recieves from
# the input field. get_input() need to have a placeholder
# for this input. print(the ouput)
def get_input(i):
    print(i)

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("Echo input", 200, 200)
frame.add_input("Enter input:", get_input, 100)

# Start the frame animation
frame.start()


###################################################
# Test

get_input("First test input")
get_input("Second test input")
get_input("Third test input")

###################################################
# Expected output from test

#First test input
#Second test input
#Third test input
