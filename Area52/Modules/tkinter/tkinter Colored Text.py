''' 
Some Tk widgets, like the label, text, and canvas widget, allow you to specify the fonts used to display 
text. This can be achieved by setting the attribute "font". typically via a "font" configuration option. 
You have to consider that fonts are one of several areas that are not platform-independent. 
The attribute fg can be used to have the text in another colour and the attribute bg can be used to change 
the background colour of the label. 
'''

from tkinter import *

root = Tk()

Label(root, 
		 text="Red Text in Times Font",
		 fg = "red",
		 font = "Times").pack()
Label(root, 
		 text="Green Text in Helvetica Font",
		 fg = "light green",
		 bg = "dark green",
		 font = "Helvetica 16 bold italic").pack()
Label(root, 
		 text="Blue Text in Verdana bold",
		 fg = "blue",
		 bg = "yellow",
		 font = "Verdana 10 bold").pack()

root.mainloop()
