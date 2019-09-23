# Ball grid slution

'''
Complete the given program template to produce a program that fills 
the canvas with a 10x10 grid of touching balls of the given size. 

You should use two for loops, 
one nested inside the other, 
placed in the draw handler.
'''

###################################################
# Student should enter code below

import simpleguitk as simplegui

BALL_RADIUS = 20
GRID_SIZE = 10
WIDTH = 2 * GRID_SIZE * BALL_RADIUS
HEIGHT = 2 * GRID_SIZE * BALL_RADIUS


# define draw
def draw(canvas):
	y = -20
	for w in range(10):
		y += BALL_RADIUS * 2
		x = BALL_RADIUS
		for h in range(10):
			canvas.draw_circle([x,y], BALL_RADIUS, 1, "White", "red")
			x += BALL_RADIUS * 2

# create frame and register handlers
frame = simplegui.create_frame("Ball grid", WIDTH, HEIGHT)
frame.set_draw_handler(draw)

# start frame
frame.start()

'''
# Given solution:
def draw(canvas):
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            canvas.draw_circle([2 * BALL_RADIUS * i + BALL_RADIUS, 2 * BALL_RADIUS *j + BALL_RADIUS], BALL_RADIUS, 1, "White", "White")

            2 * 40 * 0 + 20
            first run starts with 0
'''