# ImageClick
'''
#Load this image of an asteroid, and draw the image centered at the last mouse click. Prior to any mouse clicks, 
#the image should be drawn in the middle of the canvas. The image size is 95x93 pixels.\
# canvas.draw_image(image, center_source, width_height_source, center_dest, width_height_dest, rotation=0)
'''

import simpleguitk as simplegui

image = simplegui.load_image('http://commondatastorage.googleapis.com/codeskulptor-assets/asteroid.png')

WIDTH = 400
HEIGHT = 300
mouse_pos = [WIDTH / 2, HEIGHT / 2]

img_width = simplegui.image.get_width(image)
img_height = simplegui.image.get_height(image)

# mouseclick handler
def click(pos):
	global mouse_pos
	mouse_pos = pos
	# print(pos)

def draw_handler(canvas):
    canvas.draw_image(image, (img_width / 2 ,img_height / 2), (img_width, img_height), mouse_pos, (img_width, img_height))

frame = simplegui.create_frame('Testing', WIDTH, HEIGHT)
frame.set_draw_handler(draw_handler)
frame.set_mouseclick_handler(click)
frame.set_mousedrag_handler(click)
frame.set_canvas_background("gray")

frame.start()