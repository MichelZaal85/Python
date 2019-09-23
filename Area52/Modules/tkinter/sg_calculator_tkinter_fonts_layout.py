#
#  sg_calculator_tkinter_fonts_layout.py
#
#
#
"""
 Shows work-around for the layout problem caused by changing font size in
   the previous example.

 Fix is to create separate frames, with the column zero buttons etc in one
   frame and the other two columns in a separate 2nd frame.

"""

from tkinter import *  # change to Tkinter to work in V2.7.3

# create a root window
#
root = Tk()
root.title("Calculator")
root.geometry("550x500")

# create a frame in the window to hold other widgets
#

app = Frame(root)
#app = Frame(root, borderwidth = 2, relief = 'raised')  # use this line to see border

app.grid(row=0, column = 0)

# 2nd frame added for this program, separates the widgets in the two rightmost
#  columns from the 6 buttons, 2 labels and entry text box in the first colunm
#
app2 = Frame(root, borderwidth = 2, padx = 10)
app2.grid(row=0, column = 1)  # note this frame is in the 2nd column of root (top window)

#app2.grid(row=0, column = 1, sticky = 'S')  # uncomment to see the effect of sticky
#app2.grid(row=0, column = 1, sticky = 'N')  # uncomment to move the frame

# intialize variables
#
store = 0
operand = 0
button_width = 12


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



# switch in different font sizes and styles and see how the layout is less
#   affected than the previous example
#
helv16b = ('Helvetica 16 bold')
helv12i = ('Helvetica 12 italic')
helv8b = ('Helvetica 8 bold')
v15b = ("Verdana 15 bold")
v10b = ("Verdana 10 bold")
v8b = ("Verdana 8 bold")

myfont = v8b  # change v8 to one of the other options for a new font


#  http://www.tutorialspoint.com/python/tk_button.htm
#  http://effbot.org/tkinterbook/button.htm

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

L_t_box = Label(app2, text="Result:")
L_t_box.grid(column = 1, row = 0, padx = 6, pady = 2)

t_box = Text(app2,width = 30, height = 2)
t_box.grid(row = 0, column = 2, rowspan = 2, columnspan = 2, pady = 10, padx = 6, sticky = 'N')

L_t_disp = Label(app2, text="Display:")
L_t_disp.grid(column = 1, row = 3, padx = 6, pady = 2)

t_disp = Text(app2, width = 30, height = 12)   # was 6
t_disp.grid(row = 3, column = 2, columnspan = 2,  sticky = 'N')

scrl = Scrollbar(app2, command = t_disp.yview)
scrl.grid(row = 3, column = 2, columnspan = 2, sticky = 'N,S,E')


#  define both the Text (or Listbox or whatever) and the
#   Scrollbar before doing the .config() or it won't work
#
t_disp.config(yscrollcommand = scrl.set)
scrl.config(command = t_disp.yview)


mainloop()