# implementation of card game - Memory

import simpleguitk as simplegui, random
from math import floor as floor

exposed = []
cards = [] 
# helper function to initialize globals
def new_game():
    global cardNumbers, exposed, state, cards
    # create shuffled list of 2×8 numbers
    state = 0
    l1, l2 = [], []
    for i in range(8):
        l1.append(i)
        l2.append(i)
    cardNumbers = l1+l2 # concenate the 2 lists
    random.shuffle(cardNumbers) # shuffle concentated list
    
    # clear exposed cards
    exposed = []

    x1,y1,x2,y2 = 0,0,50,100
    for I in cardNumbers:
        cards.append([[x1, 0], [x2, 0], [x2,100], [x1,100], [x1,0], 2, 'silver', 'green',I])
        x1 += 50
        x2 += 50

     

def mouseclick(pos):
    global state, exposed, card
    click1, click2 = 0,0
    mpos = floor(pos[0] / 50)
    # if click, run the following
    
    for i in range(len(cardNumbers)):
        if mpos == i:
            print('Mouse:', mpos, 'int:', i, 'cardnum:', cardNumbers[i])
            cardNum = cardNumbers[i]
    
    print(card)

    # for card in cards:        
    #     # print(pos[0]/50,math.floor(pos[0]/50))

    #     if math.floor(pos[0] / 50) == card[6]:
    #         print('card',card[6] ,'found')
    #         print(card[5])
    #         card[5] = ''

    if state == 0:
        state = 1
        print('state', state)
        exposed.append(cardNum)
    elif state == 1:
        state = 2
        print('state', state)
        exposed.append(cardNum)
        if exposed[0] == exposed[1]:
            print('\n\nScore')
    else:
        state = 1
        print('state', state)
        exposed = []
        exposed.append(cardNum)

    print('exposed', exposed)


def draw(canvas):
    global card, Card
    num_x = 15
    x1,y1,x2,y2 = 0,0,50,100
    for num in cardNumbers:
        canvas.draw_text(num, [num_x, 70], 24, "White")
        num_x += 50

    for card in cards:
        # cards.append([[x1, 0], [x2, 0], [x2,100], [x1,100], [x1,0], 2, 'silver', 'green', i])
                          # 0       1       2           3       4     5     6         7     8

        canvas.draw_polygon([card[0], card[1], card[2], card[3], card[4]], card[5], card[6], card[7])

        if card in exposed:
            card[7] = ''


        # canvas.draw_polygon([[x1, 0], [x2, 0], [x2,100], [x1,100], [x1,0]], 2, 'silver', 'green')
        # x1 += 50
        # x2 += 50

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