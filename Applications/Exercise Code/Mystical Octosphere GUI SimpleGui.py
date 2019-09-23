import random
import simpleguitk as simplegui

msg = ''


def number_to_fortune(fortune_number):
    fortune = {
    0: 'Yes, for sure!',
    1: 'Probably yes.',
    2: 'Seems like yes..',
    3: 'Definitely not!',
    4: 'Probably not.',
    5: 'I really doubt it...',
    6: 'Not sure, check back later!',
    7: 'I really can\'t tell'}
    return fortune[fortune_number]


def message(input):
    global msg
    msg = mystical_octosphere(input)
    return msg


def mystical_octosphere(question):
    return('''
Your question was... {}
You shake the mystical octosphere.
The cloudy liquid swirls, and a reply comes into view...
The mystical octosphere says... {}
        '''.format(question, number_to_fortune(random.randint(0, 32) % 8)))


def draw(canvas):
    canvas.draw_text(msg, (10, 100), 12, "lime")


frame = simplegui.create_frame('Mystical Octosphere', 450, 100, 100)
frame.add_input('enter input', message, 100)
frame.set_draw_handler(draw)
frame.start()
