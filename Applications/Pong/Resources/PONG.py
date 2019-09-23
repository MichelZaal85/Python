# Implementation of classic arcade game Pong

import simpleguitk as simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 10
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

ball_pos = 0
ball_vel = [0,0]

paddle1_pos, paddle1_vel = 0, 0
paddle2_pos, paddle2_vel = 0, 0
score1, score2 = 0, 0


def spawn_ball(direction):
    global ball_pos, ball_vel 

    ball_pos = [WIDTH /2,HEIGHT / 2]
    ball_vel_x = random.randrange(120, 240) / 60
    ball_vel_y = random.randrange(60, 180) / 60
    if direction:
        ball_vel = [ball_vel_x,-ball_vel_y]
    else:
        ball_vel = [-ball_vel_x,-ball_vel_y]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, score1, score2

    paddle1_pos, paddle2_pos = 240, 240
    score1, score2 = 0,0
    spawn_ball(random.randrange(0,2))

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_vel, paddle2_vel

# draw mid line and gutters
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White") # left gutter
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White") # Middle line
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "white") # right gutter

# Gutters
    if ball_pos[0] <= BALL_RADIUS + HALF_PAD_WIDTH:
        if ball_pos[1] >= paddle1_pos - PAD_HEIGHT and ball_pos[1] <= paddle1_pos:
            ball_vel[0] = -ball_vel[0] # Bounce
            ball_vel[0] += ball_vel[0] / 10
            ball_vel[1] += ball_vel[1] / 10
        else:
            score2 += 1
            spawn_ball(RIGHT)

    elif ball_pos[0] >= WIDTH - BALL_RADIUS: # hits right gutter
        if ball_pos[1] >= paddle2_pos - PAD_HEIGHT and ball_pos[1] <= paddle2_pos:
            ball_vel[0] = -ball_vel[0] # Bounce
            ball_vel[0] += ball_vel[0] / 10
            ball_vel[1] += ball_vel[1] / 10
        else:
            score1 += 1
            spawn_ball(LEFT)

# Top and bottom
    elif ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    elif ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]        
    
# draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

# Check constantly if paddle goes off screen
    paddle1_pos += paddle1_vel
    if paddle1_pos - PAD_HEIGHT <= 0 or paddle1_pos >= HEIGHT:
        paddle1_vel = 0

    paddle2_pos += paddle2_vel
    if paddle2_pos - PAD_HEIGHT <= 0 or paddle2_pos >= HEIGHT:
        paddle2_vel = 0

# draw paddles
    canvas.draw_polyline([(HALF_PAD_WIDTH,paddle1_pos),(HALF_PAD_WIDTH, paddle1_pos - PAD_HEIGHT)],PAD_WIDTH,'red')
    canvas.draw_polyline([(WIDTH-HALF_PAD_WIDTH,paddle2_pos),(WIDTH-HALF_PAD_WIDTH, paddle2_pos - PAD_HEIGHT)],PAD_WIDTH,'lime')

# draw scores
    canvas.draw_text(str(score1),(125,100), 50,'white')
    canvas.draw_text(str(score2),(425,100), 50,'white')

def keydown(key):
    global paddle1_vel, paddle2_vel, paddle1_pos
 
    # Player 1 -- Lefthand side paddle
    if key == simplegui.KEY_MAP['w'] and paddle1_pos >= PAD_HEIGHT: # UP
        paddle1_vel -= 3
    if key == simplegui.KEY_MAP["s"] and paddle1_pos <= HEIGHT: # DWN
        paddle1_vel += 3

    # Player 2 -- Righthand side paddle
    if key == simplegui.KEY_MAP['up'] and paddle2_pos >= PAD_HEIGHT:
        paddle2_vel -= 3
    if key == simplegui.KEY_MAP["down"] and paddle2_pos <= HEIGHT:
        paddle2_vel += 3

def keyup(key):
    global paddle1_vel, paddle2_vel

    if key == simplegui.KEY_MAP["w"] or key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP["up"] or key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Reset", new_game, 100)

# start frame
new_game()
frame.start()