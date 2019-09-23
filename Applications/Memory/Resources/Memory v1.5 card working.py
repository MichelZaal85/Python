# implementation of card game - Memory

import simpleguitk as simplegui
import random, math

numbers = [i for i in range(8)] + [n for n in range(8)]
cards = []
exposed_cards = []
# card_color = 'red'
# exposed_cards = set()
# helper function to initialize globals

def new_game():
    x1,y1,x2,y2 = 0,0,50,100
    for i in range(16):
        cards.append([[x1, y1], [x2, y1], [x2,y2], [x1,y2], [x1,y1],'red', i])
        x1 += 50
        x2 += 50
    print('cards list:\n',cards)

# define event handlers
def mouseclick(pos):

    # print(pos)
    for card in cards:        
        # print(pos[0]/50,math.floor(pos[0]/50))

        # if math.floor(pos[0] / 50) == card[6]:
        #     print('\ncard:',card[6],'\nMouse',pos[0],'\ndiveded:',pos[0]/50, '\ncardpos',card[0][0])
        #     # card[5] = ''
        #     if card[6] not in exposed_cards:
        #         exposed_cards.append(card)
        # print(exposed_cards)
        print(card[0],card[1],card[2],card[3],card[4],card[5])


# cards are logically 50x100 pixels in size    
def draw(canvas):
    for card in cards:        
        canvas.draw_polygon([[0,0], [50,0], [50,100], [0,100], [0,0]], 2, 'silver', 'red')
        canvas.draw_polygon([card[0], card[1], card[2], card[3], card[4]], 2, 'silver', 'red')

    # num_x = 15
    # for number in numbers:
    #     canvas.draw_text(number, [num_x, 70], 24, "White")
    #     num_x += 50





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


'''
# examplecode:
# simple state example for Memory

import simplegui
     
# define event handlers
def new_game():
    global state
    state = 0
    
def buttonclick():
    global state
    if state == 0:
        state = 1
    elif state == 1:
        state = 2
    else:
        state = 1
                         
def draw(canvas):
    canvas.draw_text(str(state) + " card exposed", [30, 62], 24, "White")

# create frame and add a button and labels
frame = simplegui.create_frame("Memory states", 200, 100)
frame.add_button("Restart", new_game, 200)
frame.add_button("Simulate mouse click", buttonclick, 200)


# register event handlers
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
'''



'''
        for i in range(len(cards)): # 16
            cards.append(i)
        for card in cards:
            draw polygon([i*50],...[100],'red')
        if pos/50:
            card_color = ''
            
'''



# for i in range(len(cards)):
    # card_pos = 50 * i
    # canvas.draw_text(str(cards[i]), card_pos)

'''
returns:
0   0
.   
.   
.   
15  750
'''
