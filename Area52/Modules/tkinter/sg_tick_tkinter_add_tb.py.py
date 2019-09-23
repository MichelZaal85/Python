#
#  sg_tick_tkinter_add_tb.py
#
#  this version makes a widget Frame to hold other widgets, adds a widget
#   Text, which is a text box you can print to, and then prints
#   'tick!' inside this text box

# import simplegui

from tkinter import *     # change to Tkinter and it works in V2.7.3
root = Tk()
root.title("Tick")
root.geometry("320x400+500+300")

# create a frame in the window to hold other widgets
#
app = Frame(root)    # this is new - "Frame" is a keyword for this widget,
                     #   'app' is just a variable name I choose.
app.grid()           # three types of layout, 'grid' is the one I use here

#
#  here's a link to a good explanation of the different layout options:
#     http://www.python-course.eu/tkinter_layout_management.php


def tick():
    print ("tick!")
    t_box.insert(0.0, "\ntick!")      # added this to print to the text box
                                      #  which is called 't_box'
                                      #  0.0 means "insert print at the top'

    root.after( 1000, tick )

#timer = simplegui.create_timer(1000, tick)
#
root.after( 1000, tick )

#  next two lines define the widget t_box of type Text.  'app' is the name of
#  the Frame I made above (you can have multiple Frames with different names)
#
#  t_box.grid() places this new widget in the correct place (this is more
#   complicated as you add more widgets)
#
t_box = Text(app,width = 30, height = 20)  # width/height are given in multiples
                                           #   of the character size of the default
                                           #   system font  ... I think
                                           #   simplegui uses pixels instead
t_box.grid(row = 0, column = 0)   # comment this line out and see what happens

# timer.start()
mainloop()