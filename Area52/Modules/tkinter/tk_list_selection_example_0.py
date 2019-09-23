"""
  tk_list_selection_example_0.py
  bill
  May 23, 2013

  Examples of capturing mouse clicks on a Frame and a Canvas object in tkinter

  Starting point was http://www.codeskulptor.org/#examples-list_selection.py

  I did not use a list and did not use an equivalent to the draw handler.  Instead
    I simply drew a circle on the Canvas at each mouse click.  The original
    example would change the color from red to green if you clicked inside an
    existing circle but I'm not doing that yet.  Maybe tomorrow.

  Some key things to look for in the conversion:
    simplegui returns pos with the mouse coordinates but tkinter returns
    event.x and event.y, so you have to translate those accordingly

    Ball drawing is different.  Instead of a circle with a center point and radius
    like simplegui, tkinter requires you to draw an .oval with the upper-left
    and lower-right points defined, so another translation.

    Note I have two mouse handlers, depending on which Widget you are clicking
    in  (Canvas vs Frame).

    Notice the canvas.bind("<Button-1>", click) syntax ... Button-1 is the
    left mouse button but there are options to bind to other buttons or
    to double clicks, etc.

"""
import math
try:
    from tkinter import *
except ImportError:
    from Tkinter import *

# intialize globals
width = 450
height = 300
ball_list = []
ball_radius = 15

# helper function
def distance(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)

# define event handler for mouse click, draw  (simplegui)
"""
def click(pos):
    changed = False
    for ball in ball_list:
        if distance([ball[0], ball[1]], pos) < ball_radius:
            ball[2] = "Green"
            changed = True

    if not changed:
        ball_list.append([pos[0], pos[1], "Red"])
"""

def click(event):
    """ replacement mouse handler inside Canvas, draws a red ball on each click"""
    changed = False
    print ("Canvas: mouse clicked at ", event.x, event.y)
    for ball in ball_list:
        if distance([ball[0], ball[1]], [event.x, event.y]) < ball_radius:
            ball[2] = "Green"
            changed = True       #  I didn't use this yet

    if not changed:
        ball_list.append([event.x, event.y, "Red"])  # didn't use this either

    canvas.create_oval(event.x - ball_radius, event.y - ball_radius, \
                       event.x + ball_radius, event.y + ball_radius,\
                       width=2, fill= "Red")


def callback_frame(event):
    """ handler for mouse click in the Frame instead of the Canvas """
    print ("Frame: mouse clicked at", event.x, event.y)

"""
don't need a draw handler because the balls aren't moving
def draw(canvas):
    for ball in ball_list:
        canvas.draw_circle([ball[0], ball[1]], ball_radius, 1, "Black", ball[2])
"""

# create frame
#frame = simplegui.create_frame("Mouse selection", width, height)
#frame.set_canvas_background("White")

# register event handler
#frame.set_mouseclick_handler(click)
#frame.set_draw_handler(draw)

# start frame
#frame.start()

root = Tk()

root.title('Mouse click makes red ball')
frame = Frame(root, width = 200, height = 200)
frame.grid(column = 0, row = 1)

canvas = Canvas(root,width=200, height=200, bg='white')
canvas.grid(column = 1, row = 1)

frame.bind("<Button-1>", callback_frame)
canvas.bind("<Button-1>", click)

mainloop()
