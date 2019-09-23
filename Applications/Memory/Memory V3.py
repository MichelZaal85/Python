# implementation of card game - Memory

import simpleguitk as simplegui
import random


# helper function to initialize globals
def new_game():
    global turns

    numbers = [i for i in range(8)] + [n for n in range(8)]
    random.shuffle(numbers)


# define event handlers
def mouseclick(pos):
    # add game state logic here
    pass


# cards are logically 50x100 pixels in size
def draw(canvas):
    pass


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
