# Smile, the Game:

import simpleguitk as simplegui
import random
import math
import os

# globals
left_field, right_field = [], []
width, height = 450, 400
# ball_color = 'yellow'
# ball_border = 'black'
level = 1
smilies = 10
game_state = False
lives = 3

try:
    IMG = simplegui.load_image("https://dl.dropbox.com/s/b0aiak1mrfdj7mw/smile.png")
except Exception:
    IMG = simplegui.load_image(os.path.abspath('smile.png'))
IMG_CENTER = (50, 50)
IMG_SIZE = (100, 100)
IMG_RAD = [50, 50]


def new_game():
    global click_me, left_field, right_field, level, game_state
    level = 1
    game_state = False
    left_field, right_field = [], []
    labellevel.set_text("level:\n" + str(level))
    labelSmilies.set_text("Smilies:\n" + str(len(right_field)))
    point_creator(smilies)
    click_me = right_field[-1]
    # print(click_me)


def next_game():
    global click_me, left_field, right_field, level
    game_multipier(level)
    left_field, right_field = [], []
    level += 1
    labellevel.set_text("level:\n" + str(level))
    labelSmilies.set_text("Smilies:\n" + str(len(right_field)))
    point_creator(smilies + level)
    click_me = right_field[-1]


def game_multipier(level):
    global smilies
    if level >= 20:
        smilies *= 2
        labelSmilies.set_text("Smilies:\n" + str(len(right_field)))
    if level >= 30:
        smilies *= 3
        labelSmilies.set_text("Smilies:\n" + str(len(right_field)))


def game_over(state):
    global game_state
    if state:
        game_state = True
    else:
        game_state = False


def point_creator(n):
    for i in range(0, n):
        x = random.randint(25, width / 2 - 25)
        y = random.randint(75, height - 40)
        right_field.append((x, y))
        left_field.append((x + 225, y))


def distance(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)


def draw(canvas):
    if game_state:
        canvas.draw_text("Game Over", [width / 3 + 25, height / 3], 15, "black")
        # canvas.draw_text("Continue?", [width / 3 + 30, height / 3 + 25], 15, "black")
        # canvas.draw_image(IMG, IMG_CENTER, (IMG_SIZE), (width / 3, height / 2), IMG_RAD)
        # canvas.draw_text("Yes", [width / 4 + 20, height / 2 + 50], 15, "black")
        # canvas.draw_image(IMG, IMG_CENTER, (IMG_SIZE), (width / 3 + width / 3, height / 2), IMG_RAD)
        # canvas.draw_text("No", [width / 2 + 65, height / 2 + 50], 15, "black")
    else:
        canvas.draw_line((width / 2, 60), (width / 2, height - 10), 10, 'black')
        canvas.draw_line((0, 50), (width, 50), 2, 'black')
        canvas.draw_text("Click the extra Smilie", [10, 40], 15, "black")
        canvas.draw_text("level: " + str(level), [300, 40], 16, "lime")
        for R in right_field:
            canvas.draw_image(IMG, IMG_CENTER, (IMG_SIZE), R, IMG_RAD)
        for L in left_field[:-1]:
            canvas.draw_image(IMG, IMG_CENTER, (IMG_SIZE), L, IMG_RAD)


def click(pos):
    global ball_color
    if distance(click_me, pos) <= 20:
        next_game()
        labelSmilies.set_text("Smilies:\n" + str(len(right_field)))
        game_over(False)
    else:
        game_over(True)
        # print('game over')


frame = simplegui.create_frame("Smile, The Game", width, height)
frame.set_canvas_background("gray")
frame.add_button('New Game', new_game, width=50)
labellevel = frame.add_label('level:\n' + str(level))
labelSmilies = frame.add_label("Smilies:\n" + str(smilies))

frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)

new_game()
frame.start()
