#
#  z_flag_norway_sudan.py
#
#
#
#
#  https://www.cia.gov/library/publications/the-world-factbook/flags/flagtemplate_su.html
#  https://www.cia.gov/library/publications/the-world-factbook/flags/flagtemplate_no.html
#  https://www.cia.gov/library/publications/the-world-factbook/docs/flagsoftheworld.html
"""
 practice drawing shapes on the Canvas
"""

try:
    from tkinter import *
except ImportError:
    from Tkinter import *

root = Tk()
root.title("Flags of Norway & Sudan")
root.geometry("640x620")

width_n = 300
height_n = 200

width_s = 600
height_s = 300

Norway_canvas = Canvas(root,width=width_n, height=height_n, bg='red')
Norway_canvas.grid(row = 0, column = 0)

Sudan_canvas = Canvas(root,width=width_s + 20, height=height_s + 20, bg='gray', offset = '0,200')
Sudan_canvas.grid(row = 2, column = 0, sticky = 'se')

# had to add the dummy frame to separate the flags since 'offset = anything' doesn't work
#
#dummy_frame = Frame(root)
#dummy_frame.grid(row = 1, column = 0)

#L_blank = Label(dummy_frame, text="I'm a dummy Label")               # blank label for spacing
#L_blank.grid(column = 0, row = 0, pady = 20)


white_trim = 12
blue_trim = 6
Norway_blue = '#3366FF'


white_h = Norway_canvas.create_line(0,height_n//2,width_n,height_n//2, fill = 'white', width = height_n//3 - white_trim)
white_v = Norway_canvas.create_line(width_n//2.8,0,width_n//2.8,height_n, fill = 'white', width = height_n//3 - white_trim)

blue_h = Norway_canvas.create_line(0,height_n//2,width_n,height_n//2, fill = Norway_blue, width = height_n//6 - blue_trim)
blue_v = Norway_canvas.create_line(width_n//2.8,0,width_n//2.8,height_n, fill = 'blue', width = height_n//6 - blue_trim)


red_h   = Sudan_canvas.create_line(0,height_s//6,width_s,height_s//6, fill = 'red', width = height_s//3 )
white_h = Sudan_canvas.create_line(0,height_s//2,width_s,height_s//2, fill = 'white', width = height_s//3 )
black_h = Sudan_canvas.create_line(0,5*height_s//6,width_s,5*height_s//6, fill = 'blue', width = height_s//3)

# triangle = Sudan_canvas.create_polygon(0,0, 0, height_s, 2*width_s//4.75, height_s//2, 0,0, fill = Sudan_green)

mainloop()
