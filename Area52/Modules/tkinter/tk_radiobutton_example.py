#
#  tk_radiobutton_example.py
#
#
#
"""
simple example to show how to define one frame and one canvas, then add
 three radio buttons in the frame and print to the canvas when one is selected

option to change radio button to radio box button by changing indic and v_anchor
 variables as described below

for more info on the 38 (!!) Radiobutton options visit
  http://effbot.org/tkinterbook/radiobutton.htm
"""

try:
    from tkinter import *
except ImportError:
    from Tkinter import *

root = Tk()
root.geometry("300x180+130+180")
root.title('Radiobutton Example')

# pair 0, "center" for button box, or 1, "w" for radio button ... try 'center'
#    for radio button and see how bad it looks
#
indic = 1
v_anchor = "w"

#indic = 0
#v_anchor = "center"  #  uncomment these 2 for button box


frame1 = Frame(root)
frame1.grid(row = 0, column = 0, padx = 10)   # change padx and see the effect

# Canvas is an area of the root window where you can draw or display images
#
canvas = Canvas(root,width=200, height=180, bg='white')
canvas.grid(row = 0, column = 1)  # change to row = 1, column = 0 and see what
                                  #  happens


# simple demo of adding radio buttons to the frame and printing output
#
def rb_handler():
    """ radiobutton handler ... prints to console and canvas """
    choice = rb_var.get()  # need to understand .get to use radiobuttons!
    print (choice)
    if choice == "you selected scissors":
        canvas.itemconfig(t_canvastext, state = 'normal')
        canvas.itemconfig(t_rock, state = 'hidden')
        canvas.itemconfig(t_paper, state = 'hidden')

    elif choice == "you selected rock":
        canvas.itemconfig(t_canvastext, state = 'hidden')
        canvas.itemconfig(t_paper, state = 'hidden')
        canvas.itemconfig(t_rock, state = 'normal')

    else:
        canvas.itemconfig(t_paper, state = 'normal')
        canvas.itemconfig(t_rock, state = 'hidden')
        canvas.itemconfig(t_canvastext, state = 'hidden')

rb_var = StringVar()

#rb_var.set("you selected paper")   # uncomment this and see how buttons initialize
#rb_var.set(" ")

# let's go through the first line in detail ...
#
#  'rb_rock' is just a variable name I assigned
#  'Radiobutton' is the widget keyword
#  'frame1' tells where to place this widget
#  'text = "rock"' is the text appearing next to the button
#  'width' is the width ... especially important if using 'button box'
#  'anchor' is where the button aligns ... in this example I use 'w' or west
#      for the radio button mode and 'center' button box mode (lines 29, 32)
#  'value' is what's passed to the handler function in the .get() method
#  'command' is the event handler
#  'indicatoron' (where did they get THAT name?) selects button box or radio button mode
#       this is switched in lines 28, 31 in this example; try both
#
rb_rock = Radiobutton(frame1, text = "rock", width = 12,  anchor = v_anchor,
value = 'you selected rock', variable = rb_var, command = rb_handler, indicatoron = indic)
rb_rock.grid(row = 0, column = 0)

rb_paper = Radiobutton(frame1, text = "paper", width = 12, anchor = v_anchor,
value = 'you selected paper', variable = rb_var, command = rb_handler, indicatoron = indic)
rb_paper.grid(row = 6, column = 0)

rb_scissors = Radiobutton(frame1, text = "scissors", width = 12, anchor = v_anchor,
value = 'you selected scissors', variable = rb_var, command = rb_handler, indicatoron = indic)
rb_scissors.grid(row = 7, column = 0)

# the text messages are like we covered earlier ... separate text for each
#   line of code, controlled by configuration of 'state' variable .. awkward
#
t_canvastext = canvas.create_text(100,90, justify = 'left', fill = "red",
activefill = "blue", font =  "Helvetica -12",
text = "Scissors cuts paper,\nRock breaks scissors")
canvas.itemconfig(t_canvastext, state = 'hidden')

t_rock = canvas.create_text(100,90, justify = 'left', fill = "blue",
activefill = "blue", font =  "Helvetica -12",
text = "Rock breaks scissors,\nPaper covers rock")
canvas.itemconfig(t_rock, state = 'hidden')

t_paper = canvas.create_text(100,90, justify = 'left', fill = "green",
activefill = "blue", font =  "Helvetica -12",
text = "Paper covers rock,\nScissors cuts paper")
canvas.itemconfig(t_paper, state = 'hidden')


root.mainloop()