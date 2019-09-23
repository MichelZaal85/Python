#
#  sg_calculator_tkinter_fonts.py
#
#
#
"""
 1) adds support for specific fonts in the button names instead of relying
    on the system default font, which can vary between users and systems

    search for 'myfont' to see this new code

    change 'myfont' to some of the other variables to see the effects

Suggested improvements:

  If the fonts are big the scroll bar seems to be too long for the Display
     text box, so figure how to bind it correctly so it doesn't resize.

  Student project: how do you fix the layout issues with the scrollbar when
     a big font is chosen?

A fix for the scrollbar problem is shown in the next program.

"""

from tkinter import *  # change to Tkinter to work in V2.7.3

# intialize variables
#
store = 0
operand = 0
button_width = 12    # this is the size of the buttons in characters (not pixels)


# event handlers for calculator with a store and operand

def output():
    """prints contents of store and operand in Display box """
    print ("Store = ", store)
    print ("Operand = ", operand)
    print ("")

    entry_box.delete(0,END)     # clears input box
    t_box.delete(0.0, END)      # clears 'Result' text box
    t_box.insert(0.0, store)    # prints 'store' re


    t_disp.insert(0.0, '\n')
    t_disp.insert(0.0, "store = " + str(store))
    t_disp.insert(0.0, '\n')
    t_disp.insert(0.0, "operand = " + str(operand))
    t_disp.insert(0.0, '\n')

"""
the above lines insert at the upper-left corner of the text box, which makes
 sense for this example.  But often you want to append the text to the bottom
 of the existing text instead.  The next line shows how do that, switching
 0.0 to END

#    t_disp.insert(END, "operand = " + str(operand))   etc.

"""

# next are the event handlers, mostly unchanged from Joe's code


def swap():
    """ swap contents of store and operand"""
    global store, operand
    store, operand = operand, store
    output()

def add():
    """ add operand to store"""
    global store
    store = store + operand
    output()

def sub():
    """ subtract operand from store"""
    global store
    store = store - operand
    output()

def mult():
    """ multiply store by operand"""
    global store
    store = store * operand
    output()

def div():
    """ divide store by operand, with divide-by-zero trapping """
    global store
    try:
        store = store / operand
        output ()
    except ZeroDivisionError:  # traps on divide by zero error
        print ("Divide by zero error")


def enter_num(t):
    """ enter a new operand"""
    global operand
    str = entry_box.get()
    try:
        operand = float(str)  # checks that you input a number
        output()
    except ValueError:
        print ("Error.  Please enter a number!")


# create a root window
#
root = Tk()
root.title("Calculator")
root.geometry("450x300")

app = Frame(root)    # creates a frame inside the window 'root'
app.grid()

# this is new ... on the previous example we used the system default fonts,
#  but this can cause problems since those defaults vary widely.  Here I show
#  how to define specific fonts and sizes (choose common ones or you'll default
#  anyway)
#
#  so the next four lines just set up some possible choices, then I assign
#   one to 'myfont', which is passed to all the buttons.  This makes it easier
#   to try different things
#
helv16b = ('Helvetica 16 bold')
helv12i = ('Helvetica 12 italic')
helv4b = ('Helvetica 4 bold')
v10 = ("Verdana 10 ")
v8b = ("Verdana 8 bold")

myfont = v8b   # change v8b to a different variable name to change fonts

#   note the new parameter 'font = myfont' passed to each button

pr_button = Button(app, text = "Print", command = output, width=button_width, font=myfont)
pr_button.grid(column = 0, row = 0, padx = 2, pady = 2)

swap_button = Button(app, text = "Swap", command = swap, width=button_width, font=myfont)
swap_button.grid(column = 0, row = 1, padx = 2, pady = 2)

add_button = Button(app, text = "Add", command = add, width=button_width, font=myfont)
add_button.grid(column = 0, row = 2, padx = 2, pady = 2)

sub_button = Button(app, text = "Subtract", command = sub, width=button_width, font=myfont)
sub_button.grid(column = 0, row = 3, padx = 2, pady = 2)

mult_button = Button(app, text = "Mult", command = mult, width=button_width, font=myfont)
mult_button.grid(column = 0, row = 4, padx = 2, pady = 2)

div_button = Button(app, text = "Div", command = div, width=button_width, font=myfont)
div_button.grid(column = 0, row = 5, padx = 2, pady = 2)


L_blank = Label(app, text="")                    # blank label for spacing
L_blank.grid(column = 0, row = 6, padx = 2, pady = 2)

L_enter_num = Label(app, text="Enter number:")
L_enter_num.grid(column = 0, row = 7, padx = 2, pady = 2)

entry_box = Entry(app, width=12)
entry_box.grid(column = 0, row = 8, padx = 2, pady = 2)
entry_box.bind('<Return>', enter_num)

L_t_box = Label(app, text="Result:")
L_t_box.grid(column = 1, row = 0, padx = 6, pady = 2)

t_box = Text(app,width = 30, height = 2)
t_box.grid(row = 0, column = 2, rowspan = 2, columnspan = 2, pady = 10, padx = 6, sticky = 'N')

L_t_disp = Label(app, text="Display:")
L_t_disp.grid(column = 1, row = 3, padx = 6, pady = 2)

t_disp = Text(app, width = 30, height = 7)   # 6 with default font, 7 w/ v8
t_disp.grid(row = 3, column = 2, rowspan = 4, columnspan = 2,  sticky = 'N')

scrl = Scrollbar(app, command = t_disp.yview)
scrl.grid(row = 3, column = 2, rowspan = 4, columnspan = 2, sticky = 'N,S,E')

t_disp.config(yscrollcommand = scrl.set)
scrl.config(command = t_disp.yview)

# get frame rolling
# f.start()
mainloop()