import simpleguitk as simplegui
import random
import math

dCards, exposed, opend = {}, [], []
state, clicks, score = 0, 0, 0
card1, cardX = None, None
CARD = [50, 100]


def new_game():
    global clicks, score, exposed, opend
    clicks, score = 0, 0
    exposed, opend = [], []

    numbers = [i for i in range(8)] + [n for n in range(8)]
    random.shuffle(numbers)
    exposed.clear()

    # create cards
    x1, y1, x2, y2, xR = 0, 0, 50, 100, 15
    for i in range(len(numbers)):
        dCards[i] = [
              [x1, y1], [x2, y1],
              [x2, y2], [x1, y2],
              [x1, y1], 2,
            'silver', 'green', numbers.pop(0),
            i, xR, 70, 'white']
        x1 += 50
        x2 += 50
        xR += 50


def mouseclick(pos):
    global exposed, state, card1, clicks, score, opend, cardX
    # clicks += 1
    labelTurns.set_text("Turns: " + str(clicks))
    for c in dCards:
        if math.floor(pos[0] / 50) == c and dCards[c][9] not in exposed:
            if dCards[c][9] not in exposed:
                exposed.append(dCards[c][9])

            if state == 0:
                state = 1
                card1 = dCards[c][8]
                cardX = dCards[c][9]
            elif state == 1:
                state = 2
                clicks += 1
                if dCards[c][8] == card1:
                    score += 1
                    labelScore.set_text("Score: " + str(score))
                    opend.append(cardX)
                    opend.append(dCards[c][9])
            else:
                state = 1
                card1 = dCards[c][8]
                cardX = dCards[c][9]

            if len(exposed) > 2:
                for close in exposed:
                    dCards[close][7] = 'green'
                exposed.clear()
                exposed.append(dCards[c][9])
    for o in opend:
        dCards[o][7] = ''
        dCards[o][12] = 'yellow'


def draw(canvas):
    for card in dCards:
        canvas.draw_text(dCards[card][8],
                         [dCards[card][10], dCards[card][11]],
                         24, dCards[card][12])
        canvas.draw_polygon((dCards[card][0],
                             dCards[card][1],
                             dCards[card][2],
                             dCards[card][3],
                             dCards[card][4]),
                            dCards[card][5],
                            dCards[card][6],
                            dCards[card][7])

    for exposed_card in exposed:
        dCards[exposed_card][7] = ''


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
labelTurns = frame.add_label("Turns: " + str(clicks))
labelScore = frame.add_label("Score: " + str(score))
frame.add_button("Reset", new_game)

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
