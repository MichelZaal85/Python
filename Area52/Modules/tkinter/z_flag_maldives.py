#
#  z_flag_maldives.py
#
#   practice drawing shapes (line, arc, oval/circle) on the Canvas
#
#

#  https://www.cia.gov/library/publications/the-world-factbook/flags/flagtemplate_mv.html

try:
    from tkinter import *
except ImportError:
    from Tkinter import *

root = Tk()
root.title("Maldives Flag")
root.geometry("600x500")

width_m = 395                  # measured from screen capture
height_m = 263*width_m//395

green_height = 160*width_m//395
green_width = 296*width_m//395

crescent_height = 116*width_m//395
crescent_width = 75*width_m//395


canvas = Canvas(root,width=width_m + 10, height=height_m + 10, bg='white')
canvas.grid()

Maldive_green = '#00a650'     # from Photoshop off a screen dump of the
Maldive_red = '#ed1b24'       #   original, so should be really close


red = canvas.create_line(0,height_m//2,width_m,height_m//2, fill = 'red', width = height_m)
green = canvas.create_line(50,height_m//2,50+green_width,height_m//2, fill = 'green', width = green_height)

#  this works poorly but I left it in so you could see what create_arc does
#     (or doesn't do)
#
coord = width_m//2-crescent_width//2, height_m//2-crescent_height//2, \
        width_m//2+crescent_width//2, height_m//2+crescent_height//2
arc = canvas.create_arc(coord, start=90, extent=180, fill="white")

"""
offset = 15
coord_wc = width_m//2 - crescent_width//2-10, height_m//2 - crescent_height//2, \
        width_m//2 + crescent_width//2+20, height_m//2 + crescent_height//2
w_circle = canvas.create_oval(coord_wc, width = 0, fill= "white")

coord_gc = width_m//2 - crescent_width//2 + offset, height_m//2 - crescent_height//2 + 2, \
        width_m//2 + crescent_width//2 + offset*2, height_m//2 + crescent_height//2 - 2
g_circle = canvas.create_oval(coord_gc, width = 0, fill= Maldive_green)
"""

mainloop()