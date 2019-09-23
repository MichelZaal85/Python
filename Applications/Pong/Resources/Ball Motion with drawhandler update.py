# Ball motion with an implicit timer

import simpleguitk as simplegui

# Initialize globals
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20

ball_pos = [WIDTH / 2, HEIGHT / 2]
vel = [-1, 1] # pixels per update (1/60 seconds)

# define event handlers
# draw handler is called 60 times per second.
# so the ball_pos is updated 60 times per sec. vel[0] = -1 so update is 1/60 sec
# higer number, higher speed
def draw(canvas):
    # Update ball position
    ball_pos[0] += vel[0]
    ball_pos[1] += vel[1]

    # Draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")

# create frame
frame = simplegui.create_frame("Motion", WIDTH, HEIGHT)

# register event handlers
frame.set_draw_handler(draw)

# start frame
frame.start()



'''
# Ball motion with an explicit timer

import simplegui

# Initialize globals
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20

init_pos = [WIDTH / 2, HEIGHT / 2] # Mid of canvas
vel = [4, 3]  # pixels per tick
time = 0

# define event handlers
def tick():
    global time
    time += 1

def draw(canvas):
    # create a list to hold ball position
    ball_pos = [0, 0]

    # calculate ball position
    ball_pos[0] = init_pos[0] + time * vel[0]
    ball_pos[1] = init_pos[1] + time * vel[1]
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")

# create frame
frame = simplegui.create_frame("Motion", WIDTH, HEIGHT)

# register event handlers
frame.set_draw_handler(draw)

timer = simplegui.create_timer(100, tick)

# start frame
frame.start()
timer.start()

'''