# Display an X

###################################################
# Student should add code where relevant to the following.

import simpleguitk as simplegui 

# Draw handler
def draw(canvas):
	canvas.draw_text('X',[10,75],48,'red')

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame('Draw X', 70, 50)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()