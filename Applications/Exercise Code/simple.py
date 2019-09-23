# Display "This is easy?"

###################################################
# Student should add code where relevant to the following.

import simpleguitk as simplegui

# Draw handler
def draw(canvas):
    canvas.draw_text('This is easy?',[100,100],20,'green')

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("This is easy", 400, 200)
frame.set_draw_handler(draw)


# Start the frame animation
frame.start()

