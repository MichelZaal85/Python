# The Tkinter module, containing the Tk toolkit, has always to be imported. In our example, we import everything from Tkinter by using the asterisk symbol ("*") into our module's namespace:
from tkinter import *

# To initialize Tkinter, we have to create a Tk root widget, which is a window with a title bar and other decoration provided by the window manager. The root widget has to be created before any other widgets and there can only be one root widget.
root = Tk()

# The next line of code contains the Label widget. The first parameter of the Label call is the name of the parent window, in our case "root". So our Label widget is a child of the root widget. The keyword parameter "text" specifies the text to be shown:
# The pack method tells Tk to fit the size of the window to the given text.

# w = Label(root, text="Hello Tkinter!")
# w.pack()

Label(root, text="Hello Tkinter!").pack()

# The window won't appear until we enter the Tkinter event loop:
root.mainloop()

# Our script will remain in the event loop until we close the window. 