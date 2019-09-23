#
#  sg_calculator_tkinter_error_check.py
#
#
#
"""
 1) adds 'try - except' error trapping on division by zero and prints to the
    terminal instead of crashing.  This is in the 'div()' function.  Search
    for 'try:' to find where these were added.

 3) adds try - except error trapping if a non-numeric value is entered.  This
    is in the 'enter_num(t)' function.

Suggested improvements for you to code:

 The error checks only print out a message to the terminal but do not
    write anything to either the  Display or Result text boxes.

    Add code to display an error message to the Display text box and something
    like ****** to the Result text box (or $%!!&$#@!! depending on your mood).

http://docs.python.org/2/library/exceptions.html  a list of built-in exceptions
http://docs.python.org/2/tutorial/errors.html  more info on 'try-except-else-finally'

"""

#  http://www.codeskulptor.org/#examples-buttons.py  # this is the starting point
#
#  import simplegui   (replaced by the next line)

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
    t_box.insert(0.0, store)    # prints 'store' in Result box

    t_disp.insert(0.0, '\n')    # block prints in Display box
    t_disp.insert(0.0, "store = " + str(store))
    t_disp.insert(0.0, '\n')
    t_disp.insert(0.0, "operand = " + str(operand))
    t_disp.insert(0.0, '\n')


# next are the event handlers, mostly unchanged from Joe's code
#  except now I've added two try-except error checks

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


# create a frame called 'app' in the window to hold other widgets
#
app = Frame(root)
app.grid()

#  http://www.tutorialspoint.com/python/tk_button.htm
#  http://effbot.org/tkinterbook/button.htm

pr_button = Button(app, text = "Print", command = output, width=button_width)
pr_button.grid(column = 0, row = 0, padx = 2, pady = 2)

swap_button = Button(app, text = "Swap", command = swap, width=button_width)
swap_button.grid(column = 0, row = 1, padx = 2, pady = 2)

add_button = Button(app, text = "Add", command = add, width=button_width)
add_button.grid(column = 0, row = 2, padx = 2, pady = 2)

sub_button = Button(app, text = "Subtract", command = sub, width=button_width)
sub_button.grid(column = 0, row = 3, padx = 2, pady = 2)

mult_button = Button(app, text = "Mult", command = mult, width=button_width)
mult_button.grid(column = 0, row = 4, padx = 2, pady = 2)

div_button = Button(app, text = "Div", command = div, width=button_width)
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
t_box.grid(row = 0, column = 2, rowspan = 2, columnspan = 2, pady = 10, padx = 6, sticky = N)

L_t_disp = Label(app, text="Display:")
L_t_disp.grid(column = 1, row = 3, padx = 6, pady = 2)

t_disp = Text(app, width = 30, height = 6)
t_disp.grid(row = 3, column = 2, rowspan = 4, columnspan = 2,  sticky = 'N')

scrl = Scrollbar(app, command = t_disp.yview)
scrl.grid(row = 3, column = 2, rowspan = 4, columnspan = 2, sticky = 'N,S,E')


#  define both the Text (or Listbox or whatever) and the
#   Scrollbar before doing the .config() or it won't work
#
t_disp.config(yscrollcommand = scrl.set)
scrl.config(command = t_disp.yview)

# get frame rolling
# f.start()
#
mainloop()