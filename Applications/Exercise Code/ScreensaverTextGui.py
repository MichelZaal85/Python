# Simple "screensaver" program.

# Import modules
import simpleguitk as simplegui
import random

# Global state
message = "Ik houd van Jade"
position = [50, 50]
width = 500
height = 500
interval = 2000


# Handler for text box
def update(text):
    global message
    message = text


# Handler for timer
def tick():
    # global position 
    # global is optional, because we only edit a part of the position list. Not all of it.
    x = random.randrange(0, width)
    y = random.randrange(0, height)
    position[0] = x
    position[1] = y


# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text(message, position, 15, "Red")


# Create a frame 
frame = simplegui.create_frame("Home", width, height)

# Register event handlers
text = frame.add_input("Message:", update, 150)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(interval, tick)

# Start the frame animation
timer.start()
frame.start()
