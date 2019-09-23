# Mouseclick Handlers
# Ball Movement


# This program allows the user to move a circle around the
#	canvas using the mouse.

import simpleguitk as simplegui
import math
# Global Variables

canvas_width = 300
canvas_height = 300
point = [canvas_width / 2, canvas_height / 2]
RADIUS = 20

def draw(canvas):
    canvas.draw_circle(point, RADIUS, 5, "White", "Red")


def dist(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)


def drag(pos):
    global point
    if dist(point, pos) <= RADIUS:
    	point = pos


frame = simplegui.create_frame("Ball Drag", canvas_width, canvas_height)
frame.set_draw_handler(draw)
frame.set_mousedrag_handler(drag)
frame.start()
