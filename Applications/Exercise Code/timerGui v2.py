import simplegui 

counter = 0

# Timer handler
def tick():
    global counter
    print(counter)
    counter += 1
    
# Event handlers for buttons    
def start_handler():
    timer.start()

def stop_handler():
    timer.stop()
    
def reset_handler():
    global counter
    counter = 0

# Create frame and timer
frame = simplegui.create_frame("Counter with buttons", 200, 200)
timer = simplegui.create_timer(1000, tick)

frame.add_button('start',start_handler)
frame.add_button('stop', stop_handler)
frame.add_button('reset',reset_handler)
frame.set_draw_handler()
# Start timer
#timer.start()
frame.start()
