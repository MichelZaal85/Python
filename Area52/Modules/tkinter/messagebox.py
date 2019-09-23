from tkinter import *
from tkinter import messagebox

top = Tk()
top.geometry("110x110")
def helloCallBack():
   messagebox.showinfo( "Hello Python", "Hello World")

B = Button(top, text = "Hello", command = helloCallBack).place(x = 50,y = 50)
top.mainloop()