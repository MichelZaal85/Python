'''
# !/usr/bin/python3
from tkinter import *
from tkinter import messagebox

frame = Tk()
canvas = Canvas(frame, bg = "blue", height = 250, width = 300)

# draw part
coord = 10, 50, 240, 210
arc = canvas.create_arc(coord, start = 0, extent = 150, fill = "red")
line = canvas.create_line(10,10,200,200,fill = 'white')

# init frame and canvas
canvas.pack()
frame.mainloop()


'''



'''
# !/usr/bin/python3
from tkinter import *

root = Tk()
frame = Frame(root)
frame.pack()

bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )

redbutton = Button(frame, text = "Red", fg = "red")
redbutton.pack( side = LEFT)

greenbutton = Button(frame, text = "Brown", fg="brown")
greenbutton.pack( side = LEFT )

bluebutton = Button(frame, text = "Blue", fg = "blue")
bluebutton.pack( side = LEFT )

blackbutton = Button(bottomframe, text = "Black", fg = "black")
blackbutton.pack( side = BOTTOM)

root.mainloop()

'''


# !/usr/bin/python3
from tkinter import *

from tkinter import messagebox

top = Tk()
top.geometry("100x100")
def helloCallBack():
   msg = messagebox.showinfo( "Hello Python", "Hello World")

B = Button(top, text = "Hello", command = helloCallBack)
B.place(x = 50,y = 50)
top.mainloop()