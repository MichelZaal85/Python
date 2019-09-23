import simpleguitk as simplegui
import random, math

dCards = {}
exposed = []

def new_game():
	# create random numbers
	numbers = [i for i in range(8)] + [n for n in range(8)]
	random.shuffle(numbers)
	exposed.clear()
	
	# create cards
	x1,y1,x2,y2, xR = 0,0,50,100, 15
	for i in range(16):
		dCards[i] = [[x1, y1], [x2, y1], [x2,y2], [x1,y2], [x1,y1], 2, 'silver', 'green',numbers.pop(0), i, xR, 70, 'white']
		x1 += 50
		x2 += 50
		xR += 50

def mouseclick(pos):
	global exposed
	for c in dCards:
		if math.floor(pos[0] / 50) == c:
			print('\n')
			print('Mouse pos:\t',math.floor(pos[0] / 50))
			print('Card Index:\t', dCards[c][9])
			print('Card Number:\t', dCards[c][8])
			print('Card Pos:\t', dCards[c][0],dCards[c][1],dCards[c][2],dCards[c][3],dCards[c][4])
			print('Card Line:\t', dCards[c][5])
			print('Card color:\t', dCards[c][6],'fill color:',dCards[c][7])
			
			exposed.append(dCards[c][9])
			if len(exposed) > 2:
				exposed.clear()
				exposed.append(dCards[c][9])
	print('\nCards Exposed:',exposed)
'''
    global state
    if state == 0:
        state = 1
    elif state == 1:
        state = 2
    else:
        state = 1
'''


# 15: [[750, 0], [150, 0], [150, 100], [750, 100], [750, 0], 2, 'silver', 'green', 2, 15, 50, 70, white]
#          0 	      1 	    2 		    3 		    4	 5      6        7     8   9  10  11   12

# cards are logically 50x100 pixels in size    
def draw(canvas):
	for card in dCards:
		canvas.draw_text(dCards[card][8], [dCards[card][10], dCards[card][11]], 24, dCards[card][12])
		canvas.draw_polygon((dCards[card][0],dCards[card][1],dCards[card][2],dCards[card][3],dCards[card][4]), dCards[card][5], dCards[card][6], dCards[card][7])
        
	for exposed_card in exposed:
		dCards[exposed_card][7] = ''


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
