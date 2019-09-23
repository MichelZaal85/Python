"""
Animation of spinning card using image size manipulation
"""

import simpleguitk as simplegui
import math

# Load card sprite grid - 949x392 - source: jfitz.com
# Ace of Clubs selected
face_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")
CARD_SIZE = (73, 98)
CARD_CENTER = (CARD_SIZE[0] / 2, CARD_SIZE[1] / 2)

# Load card back image - 71x96
back_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")
BACK_SIZE = (71, 96)
BACK_CENTER = (BACK_SIZE[0] / 2, BACK_SIZE[1] / 2)

# Globals - count frame by frame rotation in degrees
spin_count = 88
spin_speed = 2
draw_position = CARD_SIZE


# Draw handler
def draw(canvas):
    global spin_count
    # Note that you cannot display images of zero size
    spin_count = (spin_count % 360) + spin_speed
    draw_width = CARD_SIZE[0] * math.sin(math.radians(spin_count))
    if spin_count < 180:
        canvas.draw_image(face_image, CARD_CENTER, CARD_SIZE,
                          draw_position, (draw_width, CARD_SIZE[1]))
    else:
        # Can't display images using negative dimensions, either
        try:
            draw_width = math.fabs(draw_width)
            canvas.draw_image(back_image, BACK_CENTER, BACK_SIZE,
                              draw_position, (draw_width, CARD_SIZE[1]))
        except ValueError:
            pass

# Create frame and register draw handler
frame = simplegui.create_frame("Spinning Card", CARD_SIZE[0] * 2, CARD_SIZE[1] * 2)
frame.set_canvas_background('Grey')
frame.set_draw_handler(draw)

# Start frame
frame.start()
