'''
Tip #1 - Getting started on step one
The program template implements the Card class for you.
The class definition includes an initialization method __init__
that is called whenever we create a card via  Card(..., ...),
several methods for accessing the fields of a Card object and a
method__str__ that is called when we want to print(out)
information about a Card object.

We have also provided a testing template that calls the provided
Card class and includes what the expected output should look like.
Cut and paste the Card class code into the template and run the
template. If the output from the run matches the output in the
comments, the implementation of the Class probably works.

As you implement the Hand class and the Deck classes, you
should go through the same testing process for the various
methods associated with these classes. Don't rush on to
implement the next step without testing first. Note that
you don't need to use the canvas to test these methods
since we have the string method available to print(out)
the information about class objects to the console.

Tip #2 - Implementing the basic Hand class
Step two asks you to implement the methods __init__,
__str__, and add_card for the Hand class. Logically,
we will think of a hand as a collection cards which
we will model in Python as a list of cards. So, to
implement the basics of a Hand class, we will need
a field in the Hand class to keep track of the list
of cards. For the sake of simplicity, let's call
that field cards.

The __init__ method should create an empty hand by
assigning an empty list to the cards field. Implementing
this method should be one line of code.
The  add_card(card) method should take the Card object
card and append it to the list in the cards field.
Implementing this method should be one line of code.
The __str__ method should return a string the includes
the string representations for each card (remember you
have a string method for Cards to turn a card into a string).
Take a look at problem 4 in the practice exercises for mouse
and list methods if you are stuck on building this string.
Before proceeding, remember to use the testing template to
check whether your Hand class is implemented correctly.

Tip #3 - Implementing the Deck class
Step three asks you to implement methods for the Deck class.
Just as in the case of the Hand class, we suggest modeling a
deck as a list of cards and keep track of that list using a
single field in the Deck class. The method deal_card can be
implemented in a single line using a common list operation.
The shuffle method can be implemented using ...) random.shuffle(...).
(Remember that random.shuffle does not return the shuffled list;
a it mutates it's parameter.) You should also implement
the __str__ method to aid in debugging.
(This implementation of this method is almost identical
to that of the string method for hands.)

The trickiest method is __init__which should return a deck
containing all 52 cards. To implement init for the Deck class,
we suggest that you use a pair of nested for-loops or a list
comprehension with two for clauses. While building these loops,
the first question that you should ask is: "What should these
loops be iterating over?". For a deck of cards, the loops
should be iterating over the entries in SUITS and RANKS.
One possible structure for the loops would be something like:
'''
'''
SUITS = {}
RANKS = {}

for suit in SUITS:
    for rank in RANKS:
        pass
        # create a Card object using Card(suit, rank)
        # and add it to the card list for the deck

'''
'''
Note that this fairly abstract operation is expressed in a
single line of code that reflects the logical structure of
"hitting" a Blackjack hand. The Hand class and the Deck
class provide us with a layer of abstraction that allows
to manipulate hands and deck at a level closer to the
true logic of Blackjack.

Tip #5 - Implementing the draw method for a hand
Part of the usefulness of object-oriented programming
is that we can use a method from one class to implement
a method from another class. In the case of the draw method
for a hand, we can use the draw method for card object.
The draw method for a hand would look something like
'''


'''
def draw(self, canvas, pos):
    for c in self.cards:
        c.draw(canvas, ...)


'''
'''
The parameter pos will determine where the hand is
drawn on the canvas. Note that for this method to
work, c must be a card object (not a string or tuple).
You need to fill in the remaining code (1 line) to
position the individual cards in some reasonable
pattern based on pos.

Tip #6 - Automated testing
Using the automated testing infrastructure that we have
built for the "Fundamentals of Computing" series, we
have built some automated unit tests for checking the
informal testing templates that are provided in the
mini-project description for Blackjack. Both the
testing templates and their corresponding automated
tests are linked below. To use one of the automated
tests, fill in your implementation of the particular
class in the testing template, save that program in
CodeSkulptor and paste the URL into appropriate
field on the unit testing page. Note that the unit
tests expect any auxiliary information like the Card
class to be included in the submitted code.

These automated test are more extensive than the manual
tests present in the testing templates. You are welcome
to post questions in this thread, especially for situations
when your code passes the informal tests, but fails the
automated tests. However, please do not post a link to
your class implementation in this thread. If necessary,
you may email your code to the Code Clinic
(interactivepython@online.rice.edu) for assistance.


Card class -- Informal testing template and automated unit test
'''
'''
# Testing template for the Card class


import random

# define globals for cards
SUITS = ['C', 'S', 'H', 'D']
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


#################################################
# Student should insert the implementation of the Card class here


###################################################
# Test code

c1 = Card("S", "A")
print(c1)
print(c1.get_suit(), c1.get_rank())
print(type(c1))

c2 = Card("C", "2")
print(c2)
print(c2.get_suit(), c2.get_rank())
print(type(c2))

c3 = Card("D", "T")
print(c3)
print(c3.get_suit(), c3.get_rank())
print(type(c3))


###################################################
# Output to console

#SA
#S A
#<class '__main__.Card'>
#C2
#C 2
#<class '__main__.Card'>
#DT
#D T
#<class '__main__.Card'>


'''
import random

# define globals for cards
SUITS = ['C', 'S', 'H', 'D']
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            print("Invalid card: ", suit, rank)

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (card_size[0] * (0.5 + RANKS.index(self.rank)), card_size[1] * (0.5 + SUITS.index(self.suit)))
        canvas.draw_image(card_images, card_loc, card_size, [pos[0] + card_size[0] / 2, pos[1] + card_size[1] / 2], card_size)


'''
#####################################################
# Student should insert code for Hand class here


'''
'''
Step two asks you to implement the methods __init__,
__str__, and add_card for the Hand class.
Logically, we will think of a hand as a collection cards which
we will model in Python as a list of cards.
So, to implement the basics of a Hand class, we will need
a field in the Hand class to keep track of the list
of cards. For the sake of simplicity, let's call
that field cards.
'''


class Hand():
    def __init__(self):
        self.cards = []

    def __str__(self):
        return str()

    def add_card(self, card):
        self.cards.append(card)

###################################################
# Test code


c1 = Card("S", "A")
c2 = Card("C", "2")
c3 = Card("D", "T")
print(c1, c2, c3)
print(type(c1), type(c2), type(c3))

test_hand = Hand()
print(test_hand)

test_hand.add_card(c1)
print(test_hand)

test_hand.add_card(c2)
print(test_hand)

test_hand.add_card(c3)
print(test_hand)

print(type(test_hand))


###################################################
# Output to console
# note that the string representation of a hand will
# vary based on how you implemented the __str__ method

#SA C2 DT
#<class '__main__.Card'> <class '__main__.Card'> <class '__main__.Card'>
#Hand contains
#Hand contains SA
#Hand contains SA C2
#Hand contains SA C2 DT
#<class '__main__.Hand'>
'''

Deck class -- Informal testing template and automated unit test
'''
# Testing template for the Deck class


'''
import random

# define globals for cards
SUITS = ['C', 'S', 'H', 'D']
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            print("Invalid card: ", suit, rank)

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (card_size[0] * (0.5 + RANKS.index(self.rank)), card_size[1] * (0.5 + SUITS.index(self.suit)))
        canvas.draw_image(card_images, card_loc, card_size, [pos[0] + card_size[0] / 2, pos[1] + card_size[1] / 2], card_size)


#####################################################
# Student should insert code for Deck class here

class Deck():
    def __init__(self, ):
        pass

    def deal_card(self):
        return self.card

    def shuffle(self):
        pass


###################################################
# Test code

test_deck = Deck()
print(test_deck)
print(type(test_deck))

c1 = test_deck.deal_card()
print(c1)
print(type(c1))
print(test_deck)

c2 = test_deck.deal_card()
print(c2)
print(type(c2))
print(test_deck)

test_deck = Deck()
print(test_deck)
test_deck.shuffle()
print(test_deck)
print(type(test_deck))

c3 = test_deck.deal_card()
print(c3)
print(type(c3))
print(test_deck)


###################################################
# Output to console
# output of string method for decks depends on your implementation of __str__
# note the output of shuffling is randomized so the exact order of cards
# need not match

#Deck contains CA C2 C3 C4 C5 C6 C7 C8 C9 CT CJ CQ CK SA S2 S3 S4 S5 S6 S7 S8 S9 ST SJ SQ SK HA H2 H3 H4 H5 H6 H7 H8 H9 HT HJ HQ HK DA D2 D3 D4 D5 D6 D7 D8 D9 DT DJ DQ DK
#<class '__main__.Deck'>
#DK
#<class '__main__.Card'>
#Deck contains CA C2 C3 C4 C5 C6 C7 C8 C9 CT CJ CQ CK SA S2 S3 S4 S5 S6 S7 S8 S9 ST SJ SQ SK HA H2 H3 H4 H5 H6 H7 H8 H9 HT HJ HQ HK DA D2 D3 D4 D5 D6 D7 D8 D9 DT DJ DQ
#DQ
#<class '__main__.Card'>
#Deck contains CA C2 C3 C4 C5 C6 C7 C8 C9 CT CJ CQ CK SA S2 S3 S4 S5 S6 S7 S8 S9 ST SJ SQ SK HA H2 H3 H4 H5 H6 H7 H8 H9 HT HJ HQ HK DA D2 D3 D4 D5 D6 D7 D8 D9 DT DJ
#Deck contains CA C2 C3 C4 C5 C6 C7 C8 C9 CT CJ CQ CK SA S2 S3 S4 S5 S6 S7 S8 S9 ST SJ SQ SK HA H2 H3 H4 H5 H6 H7 H8 H9 HT HJ HQ HK DA D2 D3 D4 D5 D6 D7 D8 D9 DT DJ DQ DK
#Deck contains CT H6 C4 H9 D6 HJ D2 S5 D8 H2 ST H4 HQ HK S8 D3 CJ D5 DK DQ DA S9 S6 S2 DJ C8 SJ C9 D4 C7 SK CK S3 CA SA S4 CQ S7 HA H3 C5 D9 DT H7 HT C2 SQ H8 C6 D7 C3 H5
#<class '__main__.Deck'>
#H5
#<class '__main__.Card'>
#Deck contains CT H6 C4 H9 D6 HJ D2 S5 D8 H2 ST H4 HQ HK S8 D3 CJ D5 DK DQ DA S9 S6 S2 DJ C8 SJ C9 D4 C7 SK CK S3 CA SA S4 CQ S7 HA H3 C5 D9 DT H7 HT C2 SQ H8 C6 D7 C3

import random

# define globals for cards
SUITS = ['C', 'S', 'H', 'D']
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            print("Invalid card: ", suit, rank)

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (card_size[0] * (0.5 + RANKS.index(self.rank)), card_size[1] * (0.5 + SUITS.index(self.suit)))
        canvas.draw_image(card_images, card_loc, card_size, [pos[0] + card_size[0] / 2, pos[1] + card_size[1] / 2], card_size)


#####################################################
# Student should insert code for Hand class here

class Hand():
    def __init__(self):
        pass

    def get_value(self):
        pass

    def add_card(self):
        pass


###################################################
# Test code

c1 = Card("S", "A")
c2 = Card("C", "2")
c3 = Card("D", "T")
c4 = Card("S", "K")
c5 = Card("C", "7")
c6 = Card("D", "A")

test_hand = Hand()
print(test_hand)
print(test_hand.get_value())

test_hand.add_card(c2)
print(test_hand)
print(test_hand.get_value())

test_hand.add_card(c5)
print(test_hand)
print(test_hand.get_value())

test_hand.add_card(c3)
print(test_hand)
print(test_hand.get_value())

test_hand.add_card(c4)
print(test_hand)
print(test_hand.get_value())


test_hand = Hand()
print(test_hand)
print(test_hand.get_value())

test_hand.add_card(c1)
print(test_hand)
print(test_hand.get_value())

test_hand.add_card(c6)
print(test_hand)
print(test_hand.get_value())

test_hand.add_card(c4)
print(test_hand)
print(test_hand.get_value())

test_hand.add_card(c5)
print(test_hand)
print(test_hand.get_value())

test_hand.add_card(c3)
print(test_hand)
print(test_hand.get_value())


###################################################
# Output to console
# note that the string representation of a hand may vary
# based on your implementation of the __str__ method

#  Hand contains
#  0
#  Hand contains C2
#  2
#  Hand contains C2 C7
#  9
#  Hand contains C2 C7 DT
#  19
#  Hand contains C2 C7 DT SK
#  29
#  Hand contains
#  0
#  Hand contains SA
#  11
#  Hand contains SA DA
#  12
#  Hand contains SA DA SK
#  12
#  Hand contains SA DA SK C7
#  19
#  Hand contains SA DA SK C7 DT
#  29
'''

'''
Tip #7 - Attribute errors
If you are getting an error like this:

'str' object has no attribute 'get_rank' AttributeError:
’str’objecthasnoattribute’get_rank’

it is (probably) because you've made a Deck and/or a
Hand that is full of strings instead of full of Cards.
Whenever you create a card you should call the Card method,
which is the same as saying the init method of the
Card class. You would say something like
'''


'''
new_card = Card(...)


'''

'''
There are only 2 methods that need this if I recall correctly.
One is the Deck method that creates a new deck. It must use
Card to make the cards.The add_card method should use the "card"
that is PASSED IN. It should NOT create a card in any way.
'''
'''
Again, test your implementation of the Deck class with the provided
testing template before proceeding.

Tip #4 - Hitting a hand using the Hand and Deck methods
In step four, you are asked to use the add_card method
for the Hand class and the deal_card method for the Deck
class to "hit" a Blackjack hand. Given a deck called
my_deck and a hand called my_hand, we can transfer
a card from my_deck to my_hand via
'''
'''
my_hand = Card()
my_deck = Deck()
my_hand.add_card(my_deck.deal_card())
