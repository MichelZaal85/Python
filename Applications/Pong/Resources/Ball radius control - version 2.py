# Challenge: 
# Complete the program template below so that holding down the up arrow key increases the radius of the white ball centered 
# in the middle of the canvas by a small fixed amount each frame. Releasing the up arrow key causes that growth to cease. 
# You will need to add code to the keydown and keyup handlers as well as the draw handler.

# Ball radius control - version 2

import simpleguitk as simplegui

WIDTH = 300
HEIGHT = 200
ball_radius = 10
ball_growth = 0
BALL_GROWTH_INC = .2

# Handlers for keydown and keyup
def keydown(key):
    global ball_growth
   
    if key == simplegui.KEY_MAP["up"]:
        ball_growth += BALL_GROWTH_INC
    else:
        ball_growth -= BALL_GROWTH_INC

def keyup(key):
    global ball_growth
    pass

    # if key == simplegui.KEY_MAP["down"] and ball_growth >= 1:
    #     ball_growth -= BALL_GROWTH_INC
    
    
# Handler to draw on canvas
def draw(canvas):
    global ball_radius

    # add code here
    
    
    # note that CodeSkulptor throws an error if radius is not positive
    canvas.draw_circle([WIDTH / 2, HEIGHT / 2], ball_radius, 1, "White", "White")

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 300, 200)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
