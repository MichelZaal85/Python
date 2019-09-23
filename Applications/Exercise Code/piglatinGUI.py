# Convert input text into Pig Latin

###################################################
# Student should add code where relevant to the following.

import simplegui 

# Pig Latin helper function
def pig_latin(word):
    """Returns the (simplified) Pig Latin version of the word."""
    
#    first_letter = word[0]
#    rest_of_word = word[1 : ]
    if word[0] in ['a','e','u','i','o']:
        return word + 'way'
    return word[1:] + word[0] + 'ay'
    # Student should complete function on the next lines.

# Handler for input field
def get_input(i):
    print(pig_latin(i))
    

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("Pig Latin translator", 200, 200)
frame.add_input('enter word', get_input, 100)

# Start the frame animation
frame.start()



###################################################
# Test

get_input("pig")
get_input("owl")
get_input("tree")

###################################################
# Expected output from test

#igpay
#owlway
#reetay


