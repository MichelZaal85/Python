# Control ball ball_pos with the arrow keys

import simpleguitk as simplegui

# initialize state
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20

ball_pos = [WIDTH / 2, HEIGHT / 2]
vel = [-300.0 / 60.0, 50.0 / 60.0]

# ball_pos = [int(width/2), int(height/2)]
# radius = 20
# velocity = 1

# event handlers
def keydown(key):
    global ball_pos
    if key == simplegui.KEY_MAP['down']:

        # vel[0] -= 1
        ball_pos[1] = ball_pos[1] + vel[0]
    elif key == simplegui.KEY_MAP['up']:

        vel[0] += 1
        # ball_pos[1] = ball_pos[1] - vel[0]
    elif key == simplegui.KEY_MAP['right']:

        # vel[1] += 1
        ball_pos[0] = ball_pos[0] + vel[1]
    elif key == simplegui.KEY_MAP['left']:

        # vel[1] -= 1
        ball_pos[0] = ball_pos[0] - vel[1]

def draw(canvas):
    ball_pos[0] += vel[0]
    ball_pos[1] += vel[1]
    # X
    if ball_pos[0] <= BALL_RADIUS or ball_pos[0] >= WIDTH - BALL_RADIUS:
        vel[0] = - vel[0]
    # Y
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= HEIGHT - BALL_RADIUS:
        vel[1] = -vel[1]

    # canvas.draw_circle(ball_pos, radius, 2, "red", "red")
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")


# create frame
frame = simplegui.create_frame("Key Handling", WIDTH, HEIGHT)

# register event handlers
frame.set_keydown_handler(keydown)
frame.set_draw_handler(draw)

# start frame
frame.start()
