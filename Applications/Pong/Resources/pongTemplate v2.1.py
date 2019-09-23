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

ball_pos = [WIDTH /2,HEIGHT / 2]
paddle1_pos = 0
paddle1_vel = 0
ball_vel = [0,0]



# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    
    ball_pos = [WIDTH /2,HEIGHT / 2]
    ball_vel_x = random.randrange(120, 240) / 60
    ball_vel_y = random.randrange(60, 180) / 60
    if direction:
        ball_vel = [ball_vel_x,ball_vel_y]
    else:
        ball_vel = [-ball_vel_x,-ball_vel_y]


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    paddle1_pos = 240

    spawn_ball(RIGHT)
    print('new game!')


def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_vel
 
        
    # draw mid line and gutters
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White") # left gutter
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White") # Middle line
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "white") # right gutter
        
    # update ball


    if ball_pos[0] <= 10:
        if ball_pos[1] >= paddle1_pos -80 and ball_pos[1] <= paddle1_pos:
            print('Paddle Hit!!')
            ball_vel[0] = -ball_vel[0]
    if ball_pos[0] <= -100: # hits left wall
        ball_vel[0] = -ball_vel[0]
    elif ball_pos[0] >= WIDTH - BALL_RADIUS: # hits right wall
        new_game()
        # ball_vel[0] = -ball_vel[0]
    

    elif ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    elif ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]        
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    # print(ball_pos[0], ball_pos[1])
    # update paddle's vertical position, keep paddle on the screen

    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # Check constantly if paddle goes off screen
    paddle1_pos += paddle1_vel
    if paddle1_pos-80 <= 0 or paddle1_pos >= 400:
        print(paddle1_pos)
        paddle1_vel = 0

    # draw paddles
    canvas.draw_polyline([(4,paddle1_pos),(4, paddle1_pos-80)],8,'red')

    # determine whether paddle and ball collide    
    # if ball_pos[0] <= 10:
    #     if ball_pos[1] >= paddle1_pos -80 and ball_pos[1] <= paddle1_pos:
    #         print('Paddle Hit!!')

    # draw scores
        
def keydown(key):
    global paddle1_vel, paddle2_vel, paddle1_pos
 
    if key == simplegui.KEY_MAP["down"] and paddle1_pos <= 400:
        paddle1_vel += 3
        # print(paddle1_pos)

    if key == simplegui.KEY_MAP['up'] and paddle1_pos >= 80:
        paddle1_vel -= 3
        # print(paddle1_pos)


def keyup(key):
    global paddle1_vel, paddle2_vel
    
    if key == simplegui.KEY_MAP["up"] or key == simplegui.KEY_MAP["down"]:
        paddle1_vel = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Reset", new_game, 100)

# start frame
new_game()
frame.start()




'''

Add code to the program template that draws a ball moving across the Pong table. 
We recommend that you add the positional update for the ball to the draw handler as shown in the second part of the 
"Motion" video. 

Add code to the function spawn_ball that spawns a ball in the middle of the table and assigns the ball 
a fixed velocity (for now). 
Ignore the parameter direction at this point. 
DONE


Add a call to spawn_ball in the function new_game which starts a game of Pong. Note that the program 
template also includes an initial call to new_game in the main body of your program to get a game going 
immediately.


Modify your code such that the ball collides with and bounces off of the top and bottom walls. Experiment 
with different hard-coded initial velocities to test your code.
DONE


Add randomization to the velocity in spawn_ball(direction) 
The velocity of the ball should be upwards and towards the right if direction == RIGHT 
and upwards and towards the left if direction == LEFT. 

The exact values for the horizontal and vertical components of this velocity should be generated using random.randrange(). 

For the horizontal velocity, we suggest a speed of around random.randrange(120, 240) pixels per second. 
For the vertical velocity, we suggest a speed of around random.randrange(60, 180) pixels per second. 
(You will need to set the signs of velocities appropriately.)

Add code to the draw handler that tests whether the ball touches/collides with the left and right gutters. 
(Remember that the gutters are offset from the left and right edges of the canvas by the width of the paddle 
as described in the "Pong" video.) When the ball touches a gutter, use either spawn_ball(LEFT) or 
spawn_ball(RIGHT) to respawn the ball in the center of the table headed towards the opposite gutter.
Next, add code that draws the left and right paddles in their respective gutters. The vertical positions of 
these two paddles should depend on two global variables. (In the template, the variables were paddle1_pos
 and paddle2_pos.)
Add code that modifies the values of these vertical positions via an update in the draw handler. The update 
should reference two global variables that contain the vertical velocities of the paddles. (In the template, 
the variables were paddle1_vel and paddle2_vel.)
Update the values of these two vertical velocities using key handlers. The "w" and "s" keys should control 
the vertical velocity of the left paddle while the "Up arrow" and "Down arrow" key should control the velocity 
of the right paddle. In our version of Pong, the left paddle moves up at a constant velocity if the "w" key is 
pressed and moves down at a constant velocity if the "s" is pressed and is motionless if neither is pressed. 
(The motion if both are pressed is up to you.) To achieve this effect, you will need to use both a keydown and 
a keyup handler to increase/decrease the vertical velocity in an appropriate manner.
Restrict your paddles to stay entirely on the canvas by adding a check before you update the paddles' vertical 
positions in the draw handler. In particular, test whether the current update for a paddle's position will 
move part of the paddle off of the screen. If it does, don't allow the update.
Modify your collision code for the left and right gutters in step 6 to check whether the ball is actually 
striking a paddle when it touches a gutter. If so, reflect the ball back into play. This collision model 
eliminates the possibility of the ball striking the edge of the paddle and greatly simplifies your collision/reflection code.
To moderately increase the difficulty of your game, increase the velocity of the ball by 10% each time it 
strikes a paddle.
Add scoring to the game as shown in the Pong video lecture. Each time the ball strikes the left or right 
gutter (but not a paddle), the opposite player receives a point and ball is respawned appropriately.
Finally, add code to new_game which resets the score before calling spawn_ball. Add a "Restart" button that 
calls new_game to reset the score and relaunch the ball.
Your final version of Pong should be remarkably similar to the original arcade Pong game. Our full implementation 
of Pong took a little more than 100 lines of code with comments. For more helpful tips on implementing this mini-project, 
please visit the Code Clinic Tips page for this mini-project.

Grading Rubric - 19 pts total (scaled to 100 pts)

1 pt - The ball spawns in the middle of the canvas with either an upward left or an upward right velocity. 
    No credit if the ball moves only horizontally left or right. Bleh, that would be boring!
2 pts - The ball bounces off of the top and bottom walls correctly. (1 pt each)
2 pts - The ball respawns in the middle of the screen when it strikes the left or right gutter but not the paddles. 
    (1 pt for each side) Give credit for this item even if the ball hits the edge of the canvas instead of the gutter.
1 pt - The left and right gutters (instead of the edges of the canvas) are properly used as the edges of the table.
1 pt - The ball spawns moving towards the player that won the last point.
2 pts - The 'w' and 's' keys correctly control the velocity of the left paddle as described above. 
    Please test each key in isolation. 
    (1 pt if the paddle moves, but in an incorrect manner in response to 'w' and 's' key presses.)
2 pts - The up and down arrows keys correctly control the velocity of the right paddle as described above. 
    Please test each key in isolation. (1 pt if the paddle moves, but in an incorrect manner in response to up 
    and down arrow key presses.)
2 pts - The edge of each paddle is flush with the gutter. (1 pt per paddle)
2 pts - The paddles stay on the canvas at all times. (1 pt per paddle)
2 pts - The ball correctly bounces off the left and right paddles. (1 pt per paddle)
1 pt - The scoring text is positioned and updated appropriately. The positioning need only approximate that in the video.
1 pt - The game includes a "Restart" button that resets the score and relaunches the ball.

'''