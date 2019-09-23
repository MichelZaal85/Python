import simpleguitk as simplegui, time

seconds = 0

def input_handler(text):
	global seconds
	seconds = int(text)


def format_time(seconds):
	# global seconds
	Min = seconds // 60
	Sec = seconds % 60
	return '%i minutes\n%i seconds' %(Min, Sec)

def draw(canvas):
    canvas.draw_text(format_time(seconds),[50,150],23, 'white')

frame = simplegui.create_frame('Format Time', 300, 300)

frame.add_input('give number:', input_handler,50)

frame.set_draw_handler(draw)
frame.start()