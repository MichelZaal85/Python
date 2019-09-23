# TkInter

from tkinter import *
from tkinter import ttk

root = Tk()
logo = PhotoImage(file = "C:/Users/ZaaJM/Dropbox/Python/Area52/TkInterGui/python_logo.gif")
small_logo = logo.subsample(5,5)


# Basics
# --------------------------------------------------------------------------------------------
'''
# Create root (parrent to store all widgets)
root = Tk()

# create a Button widget
button = ttk.Button(root, text = 'Click the button')

# create a label:
label = ttk.Label(root, text='Hello world from TkInter')

# add the Widget to the root
# call to geometry manager to place widget
button.pack()
label.pack()

# change widget text label, two ways to do this
button['text'] = 'Do not click the button'
button.config(text='Perhaps you should click')

# get all availible configurations for the widget:
button.config()


# wrap text at pixel width
label.config(wraplength=150)
# justify text, left, center, right
label.config(justify = 'center')
# Textcolor:
label.config(foreground='blue', background='yellow')
# label font:
label.config(font=('Courier', 18, 'bold'))

# Eventhandlers
# keys, clicks, input...etc

# Event Handlers
# "command" callbacks
# "bind" for command without a standard callback method
'''


# Images
# --------------------------------------------------------------------------------------------
'''
# Add Image:
# Can only handle, GIF, PGM or PPM files
logo = PhotoImage(file = "C:/Users/ZaaJM/Dropbox/Python/Area52/TkInterGui/python_logo.gif")
label.config(image = logo)
# set back to text:
# label.config(compound = 'text')
# display both image and text:
label.config(compound = 'center')


# to prevent path to img loss:
label.img = logo
label.config(image = label.img)


# the eventloop listens to any events that may occur
# Event Loop, always place at the end:
root.mainloop()
# mainloop / EventLoop, can only handle events in a
# linear way. Events are handles in order recieved
'''


# Buttons and images
# --------------------------------------------------------------------------------------------
'''
# Buttons:
root = Tk()
button = ttk.Button(root, text='Click Me!')
# call to geometry manager to place widget
button.pack()

# Create a function that is called when btn is pressed
def aCallbackFunction():
    print('You clicked me!!')

# assign the callbackfunction to the button
button.config(command = aCallbackFunction)

# simulate a buttonclick:
button.invoke()

# widget state:
button.state(['disabled'])

# what is the state of the widget?
print('Button disabled?:')
print(button.instate(['disabled']))


# if btn disabled, !disabled == invert state
if button.instate(['disabled']):
    button.state(['!disabled'])
    print('Button not disabled any more')


# add image to button:
logo = PhotoImage(file = "C:/Users/ZaaJM/Dropbox/Python/Area52/TkInterGui/python_logo.gif")
small_logo = logo.subsample(5,5)
button.config(image = small_logo, compound = LEFT)

root.mainloop()
'''


# Checkboxes and RadioButtons
# --------------------------------------------------------------------------------------------
'''
# Check and Radio Buttons:
root = Tk()
checkButton = ttk.Checkbutton(root, text = 'chocolate')
checkButton.pack()


# Properties for the buttons, can also be applied to the
# checkboxes

# the four variable classes in TkInter:
# BooleanVar
# DoubleVar
# IntVar
# StringVar

spam = StringVar()
spam.set('SPAM')
spam.get()
#                                   value assigned tot [variable] in this case, spam
checkButton.config(variable = spam, onvalue='SPAM PLEASE!', offvalue='No SPAM!')
# In the IDLE,
# checkbox on:
spam.get() # SPAM PLEASE
# checkbox off:
spam.get() # No Spam

root.mainloop()

'''
'''
# RadioBtns
# IDLE example:
breakfast = StringVar()
#                    Displayed text,    variable name    vale of the variable
ttk.Radiobutton(root, text='SPAM', variable = breakfast, value = 'SPAM').pack()
ttk.Radiobutton(root, text='Eggs', variable = breakfast, value = 'Eggs').pack()
ttk.Radiobutton(root, text='Milk', variable = breakfast, value = 'Milk').pack()
ttk.Radiobutton(root, text='Chocolate', variable = breakfast, value = 'Chocolate').pack()
# all of the radiobuttons are connected through the variable, breakfast
breakfast.get()


# update labels with radiobutton value:
checkButton.config(textvariable = breakfast)
# '''


# Input
# --------------------------------------------------------------------------------------------
# OneLine Input:
'''
root = Tk()
entry = ttk.Entry(root, width= 30)
entry.pack()
# bind()...

entry.get()
# entry field does not have a set() method
# instead use insert() and delete()
entry.delete(0, END)
entry.delte(0,1) # first char

# insert at index, value
entry.insert(0, 'string')

# create password field
entry.config(show='*')
entry.get()


entry.state(['disabled'])
# or enable:
entry.state(['!disabled'])

entry.state(['readonly'])

root.mainloop()
'''


# combobox and spinbox
# --------------------------------------------------------------------------------------------
'''
root = Tk()
month = StringVar()

combobox = ttk.Combobox(root, textvariable = month)
combobox.pack()

# Assign the values for the combobox.
# The ComboBox allows custom entry!!
# Be aware of this
combobox.config(values = (['Jan','Feb','Mrt','Apr','Mei','Jun','Jul','Aug','Sep','Okt','Nov','Dec']))

# set starting value:
month.set('Aug')
print(month.get())





year = StringVar()
Spinbox(root, from_ = 1990, to = 2014, textvariable = year).pack()
year.set(1985)


root.mainloop()
'''


# Progressbar & Scale
# --------------------------------------------------------------------------------------------
'''
root = Tk()
progressbar = ttk.Progressbar(root, orient = VERTICAL, length = 400)
progressbar.pack()

# determinate, calculate the steps.
# indeterminate, run while program runs
progressbar.config(mode='indeterminate')
progressbar.start()
progressbar.stop()

import time
progressbar.config(mode='determinate', maximum = 100.0, value = 55.0)
for i in range(10):
    progressbar.step(2)
# progressbar.config(value=75.0)


# Automaticly update the progressbar
value = DoubleVar() # float
progressbar.config(variable = value)

scale = ttk.Scale(root, orient = HORIZONTAL, length = 100, variable = value, from_ = 0.0, to = 100.0)
scale.pack()

scale.set(25.0)
scale.get()

root.mainloop()

'''


# Frames
# --------------------------------------------------------------------------------------------
'''

frame = ttk.Frame(root)
frame.config(height=100, width=200, relief=RIDGE)

# Frames:

# FLAT  - no border
# RAISED
# SUNKEN
# SOLID
# RIDGE
# GROOVE


# adding a button,
# But assigned to the top level: frame with
# the grid geometry manager. Everything inside this
# must be with the grid from now on.now

ttk.Button(frame, text='clickMe').grid()
# add padding
frame.config(padding=(30, 15))


# frame uses the pack() geometry manager!
ttk.LabelFrame(root, height=100, width=200, text='Frame It').pack()
# LabelFrame only has a solid border

frame.pack()
root.mainloop()


'''

# Creating additional top level windows
# --------------------------------------------------------------------------------------------
'''
# root = Tk()
window = Toplevel(root)
window.title('Slave to root Window')

# draworder of windows
window.lower()
window.lift(root)

# change the windows state
window.state('zoomed')
# completly hide the window
window.state('withdrawn')
# minimize window
window.state('iconic')
window.state('normal')
# ask for window state
window.state()

# Minimize window
windows.iconify()
# unminimize window
windows.deiconify()

# position the window
# geometry takes 1 string value
# size: XxY -- 640x800
# position +X+Y -- +50+80
window.geometry('640x300+10+10')

# constrains
# Allow resize window
window.resizable(False, True)

# max and min size window
window.maxsize(640, 480)
window.minsize(200, 200)

root.destroy()
window.destroy()
'''


# Paned window
# --------------------------------------------------------------------------------------------
'''
panedwindow = ttk.Panedwindow(root, orient = HORIZONTAL) # or VERTICAL
panedwindow.pack(fill = BOTH, expand = True)

frame1 = ttk.Frame(panedwindow, width=100, height=300, relief=SUNKEN)
frame2 = ttk.Frame(panedwindow, width=400, height=400, relief=SUNKEN)
frame3 = ttk.Frame(panedwindow, width=50, height=400, relief=SUNKEN)
# Height derives from the tallest panel


# expand portions:
panedwindow.add(frame1, weight=1)
panedwindow.add(frame2, weight=4)

# Control the insert location of the panel
# panedwindow.insert(index [0...), panel)
# weight , default 0
panedwindow.insert(1, frame3)

# Hide panels, does not destroy window
# index of the panel to "hide" starting at 0
panedwindow.forget(1)

root.mainloop()
'''


# Tabs Tabpages
# --------------------------------------------------------------------------------------------
'''
notebook = ttk.Notebook(root)
notebook.pack()
frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)

notebook.add(frame1, text='tab 1')
notebook.add(frame2, text='tab 2')

# add a button to frame1
ttk.Button(frame1, text='ClickTheButton').pack()


frame3 = ttk.Frame(notebook)
notebook.insert(1, frame3, text='Tab 3')

# hide the tab, index
notebook.forget(1)

# what tab is selected? get index
notebook.inex(notebook.select())

# set a tab active
notebook.select(1) # set tab 2 active


# configure a tab
notebook.tab(1, state='disabled')
notebook.tab(1, state='hidden')

# get information about tab:
notebook.tab(1, 'text')
# get all information:
notebook.tab(1)


root.mainloop()
'''


# Text Widget
# --------------------------------------------------------------------------------------------

'''
text = Text(root, width= 40, height=10)
text.pack()

# by default, wordwrap is at char to break at words:
text.config(wrap='word')



# text.get()
# get takes a special argument
# line.char
# lines start at 1, chars at 0
# 4.2 -- Line 4, char 3
# 1.0 -- first char

# end / 1.end

# get everything
text.get('1.0', 'end')
# content of first line
text.get('1.0', '1.end')

# text.insert('index', 'value\n..\n...')
text.insert('1.0 + 2 lines lineend', 'inserted message')

text.delete('1.0', '1.0 lineend')

text.replace('1.0', '1.0 lineend', 'This is a replacement line')


# disable / enable widget
text.config(state='disabled')
# prevents text edit, select is possible
text.config(state='normal')



root.mainloop()

'''

# Treeview
# --------------------------------------------------------------------------------------------
'''
treeview = ttk.Treeview(root)
treeview.pack()

treeview.insert('', '0', 'itemId1', text='First Item')
treeview.insert('', '1', 'itemId2', text='Second Item')
treeview.insert('', 'end', 'itemId3', text='Third Item')

# add image to an item, also places it under a "root" item
treeview.insert('itemId2', 'end', 'python', text='Python', image=small_logo)

# change height
treeview.config(height=5)

# move items, move items under
treeview.move('itemId2', 'itemId1', 'end')

# default items are closed
treeview.item('itemId1', open=True)

# check status: boolean value
treeview.item('itemId1', 'open')

# hide items:
treeview.detach('itemId3')
# replace item
treeview.move('itemId3', 'itemId2', '0')

# remove item
treeview.delete('itemId3')


# Adding columns

treeview.config(columns=('version'))
treeview.column('version', width=50, anchor='center')

treeview.heading('version', text='version')


# ajust width of column:
treeview.column('#0', width=150)

# add text to the version column
treeview.set('python', 'version', 'value: 3.14')

# Tags
# Tags allows you to quickly edit multiple items with the same tag
treeview.item('python', tags=('python', 'software'))
treeview.tag_configure('software', background='yellow')


# what item is selected?
# define a callback function

def callback(event):
    print('You have selected:', treeview.selection())


treeview.bind('<<TreeviewSelect>>', callback)

# configure the selection
treeview.config(selectmode='browse')  # none - no selection possible

# select / deselect a item:
treeview.selection_add('python')
treeview.selection_remove('python')
treeview.selection_toggle('python')

root.mainloop()
'''


# Menu's
# --------------------------------------------------------------------------------------------
'''

# without the given option, it will allow all menu's to be seperatble
root.option_add('*tearOff', False)


menubar = Menu(root)
root.config(menu=menubar)

file = Menu(menubar)
edit = Menu(menubar)
help_ = Menu(menubar)

menubar.add_cascade(menu=file, label='File')
menubar.add_cascade(menu=edit, label='Edit')
menubar.add_cascade(menu=help_, label='Help')

# command='function'
file.add_command(label='new', command=lambda: print('new file menu option'))
file.add_separator()
file.add_command(label='Open', command=lambda: print('open a file menu'))

edit.add_command(label='copy', command=lambda: print('copy content'))
edit.add_separator()
help_.add_command(label='help Me', command=lambda: print('Help Menu'))

file.add_command(label='Save', command=lambda: print('save it'))

# display shortkey's, does not add the shortcut
file.entryconfig('new', accelerator='Ctrl + N')

# add image to menu items:
menu_logo = logo.subsample(10, 10)
file.entryconfig('Open', image=menu_logo, compound='left')

# disable menu entrys
file.entryconfig('Open', state='disabled')


# delete menu item
file.delete('Save')

# create submenu's
save = Menu(file)
file.add_cascade(menu=save, label='Save')

# add submenu items
save.add_command(label='Save As', command=lambda: print('Save As...'))
save.add_command(label='Save All', command=lambda: print('Save All...'))


# add Radiobuttons, same for checkboxes:
choice = IntVar()
edit.add_radiobutton(label='One', variable=choice, value=1)
edit.add_radiobutton(label='Two', variable=choice, value=2)
edit.add_radiobutton(label='Three', variable=choice, value=3)

# create context menu, with cli for file menu
file.post(400, 300)

root.mainloop()
'''

#


# Canvas
# --------------------------------------------------------------------------------------------
'''

canvas = Canvas(root)
canvas.pack()

# set width and height
canvas.config(width=640, height=480)

# create a line
line = canvas.create_line(160, 360, 480, 120, fill='blue', width=5)

# edit items in the canvas
canvas.itemconfig(line, fill='red')

# get the coördinates for the line:
canvas.coords(line)
# can also be used to edit the line:
canvas.coords(line, 0, 0, 320, 240, 640, 0)
# make the line smooth
canvas.itemconfig(line, smooth=True)
# ajust the linesegements:
canvas.itemconfig(line, splinesteps=5)
# remove canvas item
canvas.delete(line)


# Shapes:
rect = canvas.create_rectangle(160, 120, 480, 360)
canvas.itemconfig(rect, fill='yellow')

oval = canvas.create_oval(160, 120, 480, 360)
canvas.itemconfig(oval, fill='green')

arc = canvas.create_arc(160, 1, 480, 240)
canvas.itemconfig(arc, start=0, extent=180, fill='red')

# create a polyline
poly = canvas.create_polygon(160, 360, 320, 480, 480, 360, fill='blue')

# add text
text = canvas.create_text(320, 240, text='Python',
                          font=('Courier', 32, 'bold'))

# add an image
image = canvas.create_image(320, 240, image=logo)
# set draworder:
canvas.lift(text)

button = Button(canvas, text='clickme')
canvas.create_window(320, 60, window=button)

# edit items after creation add tags:
canvas.itemconfig(rect, tag=('shape'))
canvas.itemconfig(oval, tag=('shape', 'round'))

canvas.itemconfig('shape', fill='gray')

root.mainloop()
'''


# Scrollbar
# --------------------------------------------------------------------------------------------
'''
text = Text(root, width=40, height=10, wrap='word')
text.grid(row=0, column=0)

scrollbar = ttk.Scrollbar(root, orient=VERTICAL, command=text.yview)
scrollbar.grid(row=0, column=1, sticky='ns')

# let the scrollbar now where the bar is
text.config(yscrollcommand=scrollbar.set)

# same goes for the xscrollcommand
# X-Scroll                    Y-Scroll
# Text                        Text
# Canvas                      Canvas
# Treeview                    Treeview
# Entry
# Spinbox and combobox



root.mainloop()
'''


# Styles
# --------------------------------------------------------------------------------------------
'''

# active
# disabled
# focus
# pressed
# selected
# background
# readonly
# alternate
# invalid
# hover


button1 = ttk.Button(root, text='Button 1')
button2 = ttk.Button(root, text='Button 2')
button1.pack()
button2.pack()

# get Styles
style = ttk.Style()

# get all themes:
style.theme_names()

# change the default style:
style.theme_use('default')


# default style == T + widgetname
# TButton == default style button

style.configure('TButton', foreground='blue')
# .TButton derive all information from TButton

style.configure('Alarm.TButton', foreground='red', font=('Arial', 24, 'bold'))
button2.config(style='Alarm.TButton')
style.map('Alarm.TButton', foreground=[('pressed', 'green'), ('disabled', 'gray')])
# button2.state(['disabled'])

root.mainloop()
'''

# MsgBox
# --------------------------------------------------------------------------------------------
'''
from tkinter import messagebox
messagebox.showinfo(title='Message in a box', message='a messagebox message')

# three types of messageboxes:
messagebox.showinfo()
messagebox.showwarning()
messagebox.showerror()


answer = messagebox.askyesno(title='yes or no?', message='do you like this window?')
print(answer)
# returns a boolean value

# other messagebox types:
messagebox.askyesno()
messagebox.askokcancel()
messagebox.askretrycancel()
messagebox.askyesnocancel()
messagebox.askquestion()


'''
# dialogs
# --------------------------------------------------------------------------------------------
'''
from tkinter import filedialog
filename = filedialog.askopenfile()
print(filename.name)

filedialog.askdirectory()
filedialog.asksaveasfile(mode)
filedialog.asksaveasfilename()


# color chooser
from tkinter import colorchooser
colorchooser.askcolor(initialcolor='#00FF00')
# returns a list with 2 items, RGB, string Hex
# when canceld, empty list!

'''

# Geometry Managers
'''
# pack()
    # pro's
        # Simplest
        # expands to fill parent window
        # stacks verticly of horizontally
    # Cons
        # limited, not for complex layouts
# parameters for pack()
# pack(fill=[X,Y,BOTH]) X
# pack(expand=True)     Y



ttk.Label(root, text='Hello TK!', background='white').pack(fill=BOTH, expand=True, side=RIGHT)
# if you need to change the widget:
# label = ttk.Label(root, text='Hello TK!', background='white')
# label.pack(fill=BOTH, expand=True, side=RIGHT)


# the widgets are stacked in order which they are called
# anchor
ttk.Label(root, text='Hello TK!', background='white').pack(expand=True, side=RIGHT, anchor='nw')
# outside padding
ttk.Label(root, text='Hello TK!', background='green').pack(expand=True, side=RIGHT, padx=10, pady=30 )
# inside padding
ttk.Label(root, text='Hello TK!', background='yellow').pack(expand=True, side=RIGHT, ipadx=10, ipady=10)


# edit all widgets in parrent:
# set all widgets in root to take the fill=BOTH and expand=True
for widget in root.pack_slaves():  # pack_slaves() gets all widgets with pack()
    widget.pack_configure(fill=BOTH, expand=True)
    # get all properties of widgets pack info
    print(widget.pack_info())

# hide widets, does not destroy the widget
label.pack_forget()


root.mainloop()
'''


'''
# Grid()
# rows, columns

# also availible:
# grid.pack_info()
# grid_forget -- hide widget
# grid_configures()
# grid_info()
# grid_forget()

# pro's
    # Easy to organize
    # typical style
# cons
    # Slightly more involved than pack()
    # more planning

# ttk.Label(root, text='Yellow', background='yellow').grid(row=1, column=1)
# ttk.Label(root, text='Blue', background='blue').grid(row=1, column=0)
# ttk.Label(root, text='Green', background='green').grid(row=0, column=0)
# ttk.Label(root, text='Orange', background='orange').grid(row=0, column=1)

# empty rows and columns are hidden. Handy to use later for adding more widgets

# columnspan and rowspan:
# sticky, n , e, s , w, or combination with the 4. == anchor to side of the cell
ttk.Label(root, text='Yellow', background='yellow').grid(row=0, column=2, rowspan=2, sticky='nesw')
ttk.Label(root, text='Blue', background='blue').grid(row=1, column=0, columnspan=2, sticky='e')
# ttk.Label(root, text='Green', background='green').grid(row=1, column=0, sticky='nesw')
ttk.Label(root, text='Orange', background='orange').grid(row=0, column=1, sticky='nesw')

# resizeable cells:
# weight
#                 row
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=3)

root.columnconfigure(2, weight=1)

# padding:
# padx=10, pady=10
ttk.Label(root, text='Green', background='green').grid(row=1, column=0, sticky='nesw', padx=10, pady=10)
# internal padding
# ipadx=..., ipady=...
root.mainloop()
'''


'''
# place

# Provides exact control of widget location and size
# relative to other widgets
# make sure the frame cannot be resized to maintain placements

# place_forget



root.geometry('640x480+200+200')

ttk.Label(root, text='Yellow', background='yellow').place(x=100, y=50, width=100, height=50)  # absolute placement
ttk.Label(root, text='Blue', background='blue').place(relx=0.5, rely=0.5, anchor=CENTER, relwidth=0.5, relheight=0.5)  # keep centered
ttk.Label(root, text='Green', background='green').place(relx=0.5, x=100, rely=0.5, y=50 )
ttk.Label(root, text='Orange', background='orange').place(relx=1.0, x=-5, y=5, anchor='ne')

root.mainloop()
'''


# callbacks
# --------------------------------------------------------------------------------------------
'''
def callback(number):
    print('you clicked number,', number)


ttk.Button(root, text='Click Me 1', command=lambda: callback(1)).pack()
ttk.Button(root, text='Click Me 2', command=lambda: callback(2)).pack()
ttk.Button(root, text='Click Me 3', command=lambda: callback(3)).pack()

# widgets with callback option:
# Button
# Checkbutton
# Radiobutton
# Spinbox
# Scale
# Scrollbar

root.mainloop()

'''


# Keyboard Events
# --------------------------------------------------------------------------------------------

'''
# Tk Event types:
# ButtonPress
# ButtonRelease
# Enter
# Leave
# Motion
# KeyPress
# KeyRelease
# FocusIn
# FocusOut

def key_press(event):
    print(f'type: type -  {event.type}')
    print(f'type: widget -  {event.widget}')
    print(f'type: char -  {event.char}')
    print(f'type: keysym -  {event.keysym}')
    print(f'type: keycode -  {event.keycode}')


def key_del(event):
    print(f'{event.char}')
    print('del key')


def key_release(event):
    print('released a key')



def pressedA(event):
    print('you have pressed "A" ')

root.bind('<KeyPress>', key_press)
root.bind('<KeyPress-Delete>', key_del)
root.bind('<KeyRelease-Right>', key_release)
# printable chars don't have to be "<escaped>"
# with an exception to <space> & <less>
# <Shift_L>, <Control_R>,<F5>,<Up>,<Return>
# <Control-Alt-Next> == Ctrl+Alt+PageDown
root.bind('a', pressedA)


def shortcut(action):
    print(action)


root.bind('<Control-c>', lambda a: shortcut('Copy'))
root.bind('<Control-v>', lambda a: shortcut('Past'))

root.mainloop()
'''



# Mouse Events
# --------------------------------------------------------------------------------------------
'''
canvas = Canvas(root, width=640, height=480, background='white')
canvas.pack()

# mousebuttons:
# 1 left
# 2 middle
# 3 right

# <Button> | <ButtonPress>  -  Any btn was pressed
# <Button-1> | <ButtonPress-1> <1> -  the left btn was pressed
# <ButtonRelease-1>
# <Double-Button-1> <Triple-Button-1>

# <Enter>       Mouse enters widget area
# <Leave>       Mouse left widget area
# <Motion>      Mouse was moved around
# <B1-Motion>   Mouse was moved with Button 1 held down


def mouse_press(event):
    global prev
    prev = event
    print(f'Type: {event.type}')
    print(f'Widget: {event.widget}')
    print(f'Btn nr: {event.num}')
    print(f'X: {event.x}')
    print(f'Y: {event.y}')
    print(f'X_root: {event.x_root}')
    print(f'Y_root: {event.y_root}')


canvas.bind('<ButtonPress>', mouse_press)


def draw(event):
    global prev
    canvas.create_line(prev.x, prev.y, event.x, event.y)
    prev = event

canvas.bind('<B1-Motion>', draw)

root.mainloop()
'''


# Virtual Events
# --------------------------------------------------------------------------------------------
'''
entry = ttk.Entry(root)
entry.pack()

# <<virtual events>>
entry.bind('<<Copy>>', lambda a: print('Copy'))
entry.bind('<<Paste>>', lambda a: print('Paste'))


entry.event_add('<<OddNumber>>', '1', '3', '5', '7', '9')
entry.bind('<<OddNumber>>', lambda e: print('Odd number'))

print(entry.event_info('<<OddNumber>>'))

# Call virtual event
entry.event_generate('<<OddNumber>>')
entry.event_generate('<<Paste>>')

# remove virtual event
enty.event_delete('<<OddNumber>>')

root.mainloop()
'''


# Multiple events
# --------------------------------------------------------------------------------------------
'''
label1 = ttk.Label(root, text='label 1')
label2 = ttk.Label(root, text='label 2')

label1.pack()
label2.pack()

label1.bind('<ButtonPress>', lambda e: print('<ButtonPress> Label 1'))
label1.bind('<1>', lambda e: print('<1> Label 1'))

root.bind('<1>', lambda e: print('<1> Root'))

# remove binding
label1.unbind('<1>')
label1.unbind('ButtonPress')

# Bind to all instances
root.bind_all('<Escape>', lambda e: print('Escape!!'))

root.mainloop()
'''

