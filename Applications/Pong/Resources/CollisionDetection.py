# A point starts at [10, 20]. 
# It repeatedly changes position by [3, 0.7] — e.g., under button or timer control. 

# Meanwhile, a rectangle stays in place. 
# Its corners are at 

# [50, 50] (upper left), 
# [180, 50] (upper right), 
# [180, 140] (lower right), and 
# [50, 140] (lower left).

# collisionline X 50 -> 180
# collisionline Y 50

# Counter with buttons

###################################################
# Student should add code where relevant to the following.

import simpleguitk as simplegui

starting_pos = [10,20]


    
# Event handlers for buttons    
def start():
	starting_pos[0] += 6
	starting_pos[1] += 1.4
	print(starting_pos[0],',',starting_pos[1])

	if starting_pos[1] >= 50:
		print('Collision!!!') 
	elif starting_pos[0] > 200 or starting_pos[0] > 180:
		print('To Far!!')

def draw_handler(canvas):
	# Draw a stopwatch
	canvas.draw_polyline([starting_pos, (13, 20.7)], 3, 'Silver')
	canvas.draw_polyline([(50, 50),(180, 50),(180, 140),(50, 140),(50, 50)],3,'red')


	    
# Create frame and timer
frame = simplegui.create_frame("Counter with buttons", 200, 200)
frame.add_button("Start", start, 100)
frame.set_draw_handler(draw_handler)

# Start timer
frame.start()
