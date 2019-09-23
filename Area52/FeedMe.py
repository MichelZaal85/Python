# FeedMe.py

import simpleguitk as simplegui
import math

canvas_width = 500
canvas_height = 400
point = [canvas_width / 2, canvas_height / 2]
RADIUS = 20

# points = [[150,150],[50,50],[75,75]]
image = simplegui.load_image('http://commondatastorage.googleapis.com/codeskulptor-assets/Race-Car.png')

balls = {1: [[100, 100], 20, 2, "White", "red", True, True],
         2: [[100, 200], 20, 2, "White", "green", True, False]}


statics = {1: [[300, 100], 20, 3, "White", "red", False]}

WIDTH = 150
HEIGHT = 150
rot = 0
vel = 0
mouse_pos = 1, 1
img_width = simplegui.image.get_width(image)
img_height = simplegui.image.get_height(image)

def click(pos):
    global mouse_pos
    mouse_pos = pos

def draw(canvas):
    for key in balls:
        canvas.draw_circle(balls[key][0], balls[key][1],
                           balls[key][2], "White", balls[key][4])

    # canvas.draw_image(image, (img_width / 2 ,img_height / 2), (img_width, img_height), mouse_pos, (img_width, img_height))

    # canvas.draw_image(image, (img_width / 2, img_height / 2), (img_width * 2, img_height * 2), mouse_pos, (WIDTH / 2, HEIGHT / 2))

    for k in statics:
        canvas.draw_circle(statics[k][0], statics[k][1],
                           statics[k][2], "White", statics[k][4])


def dist(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)


def move(ball, pos):
    if ball == pos:
        return True


def drag(pos):
    global mouse_pos
    mouse_pos = pos
    for key in balls:
        if dist(balls[key][0], pos) <= balls[key][1] and balls[key][5]:
            balls[key][0] = pos
            for k in statics:
                if dist(statics[k][0], pos) <= statics[k][1]:
                    if statics[k][1] <= 50:
                        if balls[key][6]:
                            statics[k][1] += 10
                            balls[key][0] = [100, statics[k][0][1]]
                        else:
                            statics[k][1] -= 10
                            balls[key][0] = [200, statics[k][0][1]]
                    else:
                        statics[k][1] -= 10

frame = simplegui.create_frame("Feed Me", canvas_width, canvas_height)
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)
frame.set_mousedrag_handler(drag)
frame.start()
