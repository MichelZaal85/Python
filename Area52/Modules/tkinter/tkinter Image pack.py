from tkinter import *

# root = Tk()

# img = PhotoImage(file="../../Pictures/FinishHim.png")

# Label(root, image=img).pack(side="right")

# explanation = """
# 				At present, only GIF and PPM/PGM
# 				formats are supported, but an interface 
# 				exists to allow additional image file
# 				formats to be added easily.
# 			  """
# Label(root, 
# 			justify=LEFT,
# 			padx = 10, 
# 			text=explanation).pack(side="left")

# root.mainloop()




root = Tk()
# logo = PhotoImage(file="../images/python_logo_small.gif")
img = PhotoImage(file="../../Pictures/FinishHim.png")

Label(root, 
          compound = CENTER,
          text="""At present, only GIF and PPM/PGM
					formats are supported, but an interface 
					exists to allow additional image file
					formats to be added easily.""", 
          image=img).pack(side="right")

root.mainloop()

# We can have the image on the right side and the text left justified with a padding of 10 pixel on the left and right side by changing the Label command like this: 
'''
w = Label(root, 
		  justify=LEFT,
		  compound = LEFT,
		  padx = 10, 
		  text=explanation, 
		  image=logo).pack(side="right")
'''
