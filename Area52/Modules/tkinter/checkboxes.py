from tkinter import *
frame = Tk()

def checkboxValue():
   # print("male: %d,\nfemale: %d" % (var1.get(), var2.get()))
   print(var1.get(), var2.get(), var3.get())
   # for i in 

var1, var2, var3 = IntVar(), IntVar(), IntVar()


Label(frame, text="Your sex:").grid(row=0, sticky=W)

# var1 = IntVar()
Checkbutton(frame, text="male", variable=var1).grid(row=1, sticky=W)

# var2 = IntVar()
Checkbutton(frame, text="female", variable=var2).grid(row=2, sticky=W)

# var3 = IntVar()
Checkbutton(frame, text="Other", variable=var3).grid(row=3, sticky=W)


Button(frame, text='Quit', command=frame.quit).grid(row=4, sticky=W, pady=4)
Button(frame, text='Show', command=checkboxValue).grid(row=5, sticky=W, pady=4)

mainloop()