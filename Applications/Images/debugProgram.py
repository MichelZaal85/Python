# Image debugging problem

# draw_image(image, center_source, width_height_source, center_dest, width_height_dest, rotation=0)

###################################################
# Student should enter code below

# import simpleguitk as simplegui

# # load test image
# test_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/Race-Car.png")
# test_image_size = [135, 164]
# test_image_center = [150,150]

# # draw handler
# def draw(canvas):
#     canvas.draw_image(test_image, test_image_center, test_image_size, test_image_center, test_image_size)

# # create frame and register draw handler    
# frame = simplegui.create_frame("Test image", 300, 300)


# # start frame
# frame.start()

import simpleguitk as simplegui

image = simplegui.load_image('http://commondatastorage.googleapis.com/codeskulptor-assets/Race-Car.png')

WIDTH = 100
HEIGHT = 100
rot = 0
vel = 0

img_width = simplegui.image.get_width(image)
img_height = simplegui.image.get_height(image)

def draw_handler(canvas):
    global rot
    rot += vel
    canvas.draw_image(image, (img_width / 2 ,img_height / 2), (img_width, img_height), (WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT), rotation=rot)

def keydown_handler(key):
	global vel
	if key == simplegui.KEY_MAP['down'] or key == simplegui.KEY_MAP['right']:
		vel = .1
	if key == simplegui.KEY_MAP['up'] or key == simplegui.KEY_MAP['left']:
		vel = -.1
def keyup_handler(key):
	global vel
	vel = 0

frame = simplegui.create_frame('Testing', WIDTH, HEIGHT)
frame.set_keydown_handler(keydown_handler)
frame.set_keyup_handler(keyup_handler)
frame.set_draw_handler(draw_handler)
frame.start()

