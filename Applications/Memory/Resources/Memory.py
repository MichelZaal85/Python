# implementation of card game - Memory

import simpleguitk as simplegui
import random, math

# numbers = [i for i in range(8)] + [n for n in range(8)]
# numbers = random.sample(range(8),8) + random.sample(range(8),8)
# cards = []
# exposed = []
# state = 0
# helper function to initialize globals

def new_game():
    global exposed, cards, numbers, state
    state = 0
    exposed = []
    numbers = []
    cards = []
    integer = 0
    # create random list of numbers.
    numbers = random.sample(range(8),8) + random.sample(range(8),8)
    
    x1,y1,x2,y2 = 0,0,50,100
    for i in numbers:
        cards.append([[x1, 0], [x2, 0], [x2,100], [x1,100], [x1,0],'red', integer, state,i])
        integer += 1
        x1 += 50
        x2 += 50

def mouseclick(pos):
    global cards, state
    for card in cards:
        if math.floor(pos[0] / 50) == card[6]:
            
            if card[6] not in exposed:
                exposed.append(card)
            
            if state == 0 or state == 1:
                card[5] = ''
            else:
                for exposed_card in exposed:
                    exposed_card[5] = 'red'
                    card[5] = ''
                    
            
            # print('card state:',state, exposed)
            print('card state:',state, ', list num:', card[6], 'cardnum:', card[8], 'int:', card[7])
    
    if state == 0:
        card[5] = 'red'
        state = 1
    elif state == 1:
        state = 2
    else:
        # TODO: add code to check if exposed card values are equal
        card[5] = 'red'
        state = 1




# cards are logically 50x100 pixels in size    
def draw(canvas):
    global state
    integer = 0
    num_x = 15
    for number in numbers:
        canvas.draw_text(number, [num_x, 70], 24, "White")
        num_x += 50

    x1,y1,x2,y2 = 0,0,50,100
    for i in numbers:
        cards.append([[x1, 0], [x2, 0], [x2,100], [x1,100], [x1,0],'red', integer, state,i])
        integer += 1
        x1 += 50
        x2 += 50

    for card in cards:
        canvas.draw_polygon([card[0], card[1], card[2], card[3], card[4]], 2, 'silver', card[5])
    
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