import simpleguitk as simplegui

total_ticks = float(0.00)
first_click = True

# Timer handler
def tick():
    global total_ticks
    total_ticks += 1
    
# Event handlers for buttons    
def start():
    global first_click, total_ticks
    if first_click:
    	first_click = False
    	timer.start()
    else:
    	first_click = True
    	timer.stop()
    	print("Time between clicks is " + str(total_ticks / 100.0) + " seconds")
    	total_ticks = 0

def reset():
	global total_ticks, first_click
	total_ticks = 0
	first_click = True
	timer.stop()


# Create frame and timer
frame = simplegui.create_frame("Reflex tester", 200, 200)
frame.add_button('Click Me', start, 100)
frame.add_button('Reset me', reset, 100)
timer = simplegui.create_timer(10, tick)

frame.start()










# # Reflex tester solution code

# ###################################################
# # Student should add code where relevant to the following.

# import simpleguitk as simplegui

# total_ticks = 0
# first_click = True


# # Timer handler
# def tick():
#     global total_ticks
#     total_ticks += 1
    
# # Button handler
# def click():
#     global total_ticks, first_click
#     if first_click:
#         first_click = False
#         total_ticks = 0
#         timer.start()
#     else:
#         first_click = True
#         timer.stop()
#         print("Time between clicks is " + str(total_ticks / 100.0) + " seconds")
#         total_ticks = 0

# # Create frame and timer
# frame = simplegui.create_frame("Counter with buttons", 200, 200)
# frame.add_button("Click me", click, 200)
# timer = simplegui.create_timer(10, tick)

# # Start timer
# frame.start()
