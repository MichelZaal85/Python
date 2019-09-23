'''
import simplegui
def key_handler(key):
    …
frame = simplegui.create_frame('Testing', 100, 100)
frame.set_keydown_handler(key_handler)
frame.start()

# frame.set_keydown_handler(key_handler)
# frame.set_keyup_handler(key_handler)

# Opens frame with active keydown handler

These add keyboard event handlers waiting for keydown, 
and keyup events, respectively. 

When any key is pressed, the keydown handler is called once. 
When any key is released, the keyup handler is called once.

The handler for each should be defined with one parameter, 
as in the above example. This parameter will receive an 
integer representing a keyboard character.
'''


# Keyboard echo

import simpleguitk as simplegui

# initialize state
current_key = ' '

# event handlers
def keydown(key):
    global current_key
    current_key = chr(key)

def keyup(key):
    global current_key
    current_key = ' '
    
def draw(canvas):
    canvas.draw_text(current_key, [10, 45], 20, "Red")
    
# create frame
frame = simplegui.create_frame("Echo", 35, 35)

# register event handlers
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_draw_handler(draw)

# start frame
frame.start()
