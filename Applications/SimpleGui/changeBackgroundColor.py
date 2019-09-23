# Counter with buttons

###################################################
# Student should add code where relevant to the following.

# Use a timer to toggle the canvas background back and 
# forth between red and blue every 3 seconds. 

import simpleguitk as simplegui

color = "Red"

# Timer handler
def tick():
    frame.set_canvas_background('Blue')

# Create frame and timer
frame = simplegui.create_frame("Counter with buttons", 200, 200)
timer = simplegui.create_timer(3000, tick)

# Start timer
frame.start()
timer.start()