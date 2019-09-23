import random


def number_to_fortune(fortune_number):
    fortune = {
    0: 'Yes, for sure!',
    1: 'Probably yes.',
    2: 'Seems like yes...',
    3: 'Definitely not!',
    4: 'Probably not.',
    5: 'I really doubt it...',
    6: 'Not sure, check back later!',
    7: 'I really can\'t tell'}
    return fortune[fortune_number]


def mystical_octosphere(question):
    print('''
    Your question was...', {}
    You shake the mystical octosphere.
    The cloudy liquid swirls, and a reply comes into view...
    The mystical octosphere says... {}
    '''.format(question, number_to_fortune(random.randint(0, 100) % 8)))


mystical_octosphere("Will I get rich?")
mystical_octosphere("Are the Cubs going to win the World Series?")
mystical_octosphere('You always need Chocolate?')
input('press enter to exit')