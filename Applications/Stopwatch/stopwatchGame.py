# Stopwatch: The Game

# I've tested the following on Firefox, Chrome, Linux and Windows.
# IE, like most things, doesn't work...

# import the magic
import simpleguitk as simplegui

# t is for time
t = 0
# x is for successful stops  
x_counter = 0
# y is for total stops
y_counter = 0

# helper function to format time
def format(time):
	minsec = time % 10
	secs = (time // 10) % 60
	minutes = time // 600
	# the str().rjust creates a placeholder -- ('string').rjust(num of placeholders, "what to use as placeholder")
	return '%s:%s.%s' %(str(minutes).rjust(2,'0'), str(secs).rjust(2,'0'), str(minsec))

# Tha ticker
def tick():
	global t
	t += 1

# Start me button
def start_btn():
	if not timer.is_running():
		timer.start()

# Stop me button
def stop_btn():
	global x_counter, y_counter
	if timer.is_running():
		timer.stop()
		y_counter += 1
		# Scoreboard functionality
		if not (t % 10):
			x_counter += 1

# If your done playing button
def reset_btn():
	global t, x_counter, y_counter
	timer.stop()
	t, x_counter, y_counter = 0, 0, 0

# create timer
timer = simplegui.create_timer(100, tick)

# define draw handler
def draw_handler(canvas):
	# Draw a stopwatch
	canvas.draw_polyline([(144, 67), (356, 67), (435, 145), (435,322), (368, 437), (132, 437), (65, 322), (65, 145), (144, 67)], 3, 'Silver')
	
	# draw the time placeholder
	canvas.draw_polygon([(125, 184), (375, 184), (375, 284), (125,284), (125, 184)], 2, 'silver')

	# draw the 2 little buttons
	canvas.draw_polygon([(104, 78), (118, 92), (91, 120), (77,106), (104, 78)], 2, 'Silver','lime')
	canvas.draw_polygon([(382, 92), (396, 78), (423, 106), (409,120), (382, 92)], 2, 'silver','red')

	# draw timer_text
	canvas.draw_text(format(t), (135,274), 50, 'Lime')
	# draw scoreboard
	canvas.draw_text(str(x_counter) + '/' + str(y_counter),(300,150), 25,'green')
	canvas.draw_text('Stopwatch, The Game',(135, 410),15,'gray')

# create frame
frame = simplegui.create_frame('Stopwatch, The Game', 500,500)

# register event handlers
frame.add_button('Start', start_btn, 50)
frame.add_button('Stop', stop_btn, 50)
frame.add_button('Reset', reset_btn, 50)
frame.set_draw_handler(draw_handler)

# start frame
frame.start()

# http://www.codeskulptor.org/#user43_Vnd9rmpfxB_6.py

'''

Codeskultor code:

# Stopwatch: The Game
import simplegui
# define global variables
t = 0
x_counter = 0
y_counter = 0

# helper function to format time
def format(time):
	minsec = time % 10
	secs = (time // 10) % 60
	minutes = time // 600
	# the str().rjust creates a placeholder -- ('string').rjust(num of placeholders, "what to use as placeholder")
	return '%s:%s.%s' %(str(minutes).rjust(2,'0'), str(secs).rjust(2,'0'), str(minsec))

# Tha ticker
def tick():
	global t
	t += 1

# Start me button
def start_btn():
	if not timer.is_running():
		timer.start()

# Stop me button
def stop_btn():
	timer.stop()
	global x_counter, y_counter
	
	# Scoreboard functionality
	if not ((t // 10) % 2):
		print((t//10)%2)
		print('seconds win!')
		x_counter += 1
	elif not (t):
		print('milisec Win!')
		print(t)
		y_counter += 1

# If your done playing button
def reset_btn():
	global t, x_counter, y_counter
	timer.stop()
	t = 0
	x_counter, y_counter = 0, 0

# create timer
timer = simplegui.create_timer(100, tick)

# define draw handler
def draw_handler(canvas):
	# Draw a stopwatch
	canvas.draw_polyline([(144, 67), (356, 67), (435, 145), (435,322), (368, 437), (132, 437), (65, 322), (65, 145), (144, 67)], 2, 'Red')
	# draw the time placeholder
	canvas.draw_polyline([(125, 184), (375, 184), (375, 284), (125,284), (125, 184)], 2, 'Red')
	# draw the 2 little buttons
	canvas.draw_polyline([(104, 78), (118, 92), (91, 120), (77,106), (104, 78)], 2, 'Red')
	canvas.draw_polyline([(382, 92), (396, 78), (423, 106), (409,120), (382, 92)], 2, 'Red')

	# draw timer_text
	canvas.draw_text(format(t), (135,260), 75, "Lime")
	# draw scoreboard
	canvas.draw_text(str(x_counter) + '/' + str(y_counter),(300,150), 25,'green')


# create frame
frame = simplegui.create_frame('Stopwatch The Game', 500,500,100)

# register event handlers
frame.add_button('Start', start_btn, 50)
frame.add_button('Stop', stop_btn, 50)
frame.add_button('Reset', reset_btn, 50)
frame.set_draw_handler(draw_handler)

# start frame
frame.start()
'''