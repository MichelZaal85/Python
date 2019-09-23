# Load and rotate image
import simpleguitk as simplegui

image = simplegui.load_image('http://commondatastorage.googleapis.com/codeskulptor-assets/Race-Car.png')

WIDTH = 150
HEIGHT = 150
rot = 0
vel = 0

img_width = simplegui.image.get_width(image)
img_height = simplegui.image.get_height(image)


def draw_handler(canvas):
    global rot
    rot += vel
    canvas.draw_image(image, (img_width / 2, img_height / 2),
                      (img_width, img_height),
                      (WIDTH / 2, HEIGHT / 2),
                      (WIDTH, HEIGHT), rotation=rot)


def keydown_handler(key):
    global vel
    if key == simplegui.KEY_MAP['up'] or key == simplegui.KEY_MAP['right']:
        vel = .05
    if key == simplegui.KEY_MAP['down'] or key == simplegui.KEY_MAP['left']:
        vel = -.05


def keyup_handler(key):
    global vel
    vel = 0


frame = simplegui.create_frame('Testing', WIDTH, HEIGHT)
frame.set_draw_handler(draw_handler)
frame.set_keydown_handler(keydown_handler)
frame.set_keyup_handler(keyup_handler)
frame.start()
