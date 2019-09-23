# implementation of card game - Memory

import simpleguitk as simplegui
import random, math

numbers = [i for i in range(8)] + [n for n in range(8)]
cards = []
card_color = 'red'
# exposed_cards = set()
exposed_cards = []
# helper function to initialize globals

def new_game():

    for i+50 in range(16):
        cards.append([[i*50,0],[i*50,100],45,'red'])

# define event handlers
def mouseclick(pos):
    global card_color

# cards are logically 50x100 pixels in size    
def draw(canvas):
    global card_color

    for card in cards:
        canvas.draw_polyline([card[0],card[1]],card[2],card[3])

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