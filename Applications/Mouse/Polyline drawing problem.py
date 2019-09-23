# Polyline drawing problem

###################################################
# Student should enter code below

'''
Challenge: Write a program that draws a polyline 
(an open polygon) based on a sequence of mouse clicks. 
The first click should create a point. 
Subsequent clicks should add a new segment to 
the polyline. You should include a "Clear" 
button that deletes the polyline and restarts 
the drawing process.
'''

import simpleguitk as simplegui
import math

polyline = []
point =[0,0]

# define mouseclick handler
def click(pos):
	global polyline
	if polyline:
		point = list(pos)
	polyline.append(list(pos))


# button to clear canvas
def clear():
	global polyline
	polyline = []
	point = [0,0]

# define draw
def draw(canvas):
	global polyline, point
	
	if point != [0,0]:
		canvas.draw_point(point)
	canvas.draw_polyline(polyline, 5,'red')


# create frame and register handlers
frame = simplegui.create_frame("Echo click", 300, 200, 300)
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)
frame.add_button("Clear", clear, 100)

# start frame
frame.start()
