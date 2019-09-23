'''
simplegui draw handler 60 frames sec. 
Draw handlers update the canvas using a collection of draw commands that draw_text.. etc. 

top left 0,0
simplegui.create_frame('title',width,height)
'''


# first example of drawing on the canvas

import simpleguitk as simplegui

# define draw handler
def draw(canvas):
    # canvas.draw_text('text', point, font_size, font_color)
    canvas.draw_text("Hello!",[100, 100], 24, "White")
    canvas.draw_circle([100, 100], 2, 2, "Red")

# create frame
frame = simplegui.create_frame("Text drawing", 300, 200)

# register draw handler    
frame.set_draw_handler(draw) # gives canvas parameter to draw function

# start frame
frame.start()


'''
frame
frame.set_draw_handler(draw) takes a function argument
function argument [draw] takes a
'''