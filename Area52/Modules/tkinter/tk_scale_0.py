
"""
Name:  tk_scale_0.py

Author:  Bill Hilton

Purpose:  Demo of tkinter Scale widget, intended as an improvement for the
           Guess the Number tkinter version

Created: May 22, 2013

License:  feel free to use any way you wish

  quick intro to Scale widget

    To demo, move the sliders and then press the button.  The values will
    print to the interpreter window.

    Shows how to create a Scale widget and then 'get' a value when the
    button is pushed.  You could use this in Guess the Number to
    avoid having to use the Entry box widget.   Just substitute the 'get'
    value for the text entry box value.

    Note you won't get an error for entering a string or out-of-range
    value because you are limited to a defined range

    Note the use of from_ in the Scale parameter list ... apparently 'from'
    is a Python reserved word, so don't delete the trailing _ in from_.

    This was checked as-is in both Python 2.7.3 and 3.2.3

    """
try:
    from tkinter import *
except ImportError:
    from Tkinter import *

master = Tk()

def get_scale_val():
    """ button handler, 'gets' the values from both scales when button is pressed """
    guess_h = w_h.get()
    print ("You guessed (horizontal) ", guess_h)
    guess_v = w_v.get()
    print ("You guessed (vertical) ", guess_v)

w_v = Scale(master, from_= 0, to=1000)    # vertical (default) scale
w_v.pack()

w_h = Scale(master, from_= 0, to=200, orient=HORIZONTAL)  # horizontal scale
w_h.pack()

enter_val = Button(master, text = "Enter Value", command = get_scale_val)
enter_val.pack()

mainloop()

