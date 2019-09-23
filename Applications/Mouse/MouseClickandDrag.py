# Echo mouse click in console

###################################################
# Student should enter code below
import simpleguitk as simplegui

def mouse_handler(position):
	print('Mouse click at',position)


frame = simplegui.create_frame('Click Me Echo',300,300)
frame.set_mouseclick_handler(mouse_handler)
frame.set_mousedrag_handler(mouse_handler)

frame.start()

###################################################
# Sample output

#Mouse click at (104, 105)
#Mouse click at (169, 175)
#Mouse click at (197, 135)
#Mouse click at (176, 111)
#Mouse click at (121, 101)
#Mouse click at (166, 208)
#Mouse click at (257, 235)
#Mouse click at (255, 235)