# Mini-project #6 - Blackjack - By Michel Zaal

import simpleguitk as simplegui
import random

# load card sprite - 950x392 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

BACK_SIZE = [72, 96]
BACK_CENTER = [36, 48]
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")

HEIGHT = 600
WIDTH = 600

in_play = False
outcome = ''
msg = ''
score = 0

SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
          '9': 9, 'T': 10, 'J': 10, 'Q': 10, 'K': 10}


class Card():
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            print("Invalid card: ", self.suit, self.rank)

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos, img):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank),
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(img,
                          card_loc, CARD_SIZE,
                          [pos[0] + CARD_CENTER[0],
                           pos[1] + CARD_CENTER[1]], CARD_SIZE)


class Hand():
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def __str__(self):
        hand = ''
        for c in (self.cards):
            hand += c.get_suit() + c.get_rank() + ' '
        return 'The hand contains ' + hand

    def get_value(self):
        hand_value = 0
        ace = False
        for card in self.cards:
            hand_value += VALUES[card.get_rank()]
            if 'A' in card.get_rank():
                ace = True
        if ace and (hand_value + 10) <= 21:
            return hand_value + 10
        return hand_value

    def busted(self):
        if self.get_value() > 21:
            # print('Your busted!')
            return True

    def draw(self, canvas, pos):
        for card in self.cards:
            pos[0] += 100
            card.draw(canvas, [pos[0], pos[1]], card_images)

    def hold(self, canvas, pos):
        if in_play:
            pos[0] += 100
            canvas.draw_image(card_back,
                              (BACK_CENTER[0], BACK_CENTER[1]),
                              (BACK_SIZE[0], BACK_SIZE[1]),
                              (BACK_CENTER[0] + pos[0],
                               BACK_CENTER[1] + pos[1]),
                              (BACK_SIZE[0], BACK_SIZE[1]))


class Deck():
    def __init__(self):
        self.deck = []
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        return self.deck.pop()

    def __str__(self):
        deck = ''
        for card in (self.deck):
            deck += card.get_suit() + card.get_rank() + ' '
        return 'Deck contains ' + deck


def deal():
    global outcome, msg, in_play, player_hand, dealer_hand, game_deck, score

    if in_play:
        score -= 1
    outcome = ''
    msg = 'Hit or Stand?'
    in_play = True

    game_deck = Deck()
    game_deck.shuffle()

    player_hand = Hand()
    dealer_hand = Hand()

    for card in range(2):
        player_hand.add_card(game_deck.deal_card())
        dealer_hand.add_card(game_deck.deal_card())
        print()
    print('Player hand:', player_hand.get_value())


def hit():
    global player_hand, in_play, outcome, score, msg
    if in_play:
        if player_hand.get_value() != 21:
            player_hand.add_card(game_deck.deal_card())
        else:
            in_play = False
            outcome = "You've Won!"
        print('Player hand:', player_hand.get_value())
        if player_hand.busted():
            print('Busted! Game Over')
            outcome = "You're Busted..."
            msg = 'New Game?'
            in_play = False
            score -= 1
    else:
        outcome = "Press 'Deal'\nto start new game"
        return


def stand():
    global player_hand, in_play, dealer_hand, outcome, msg, score
    if not in_play:
        outcome = "Press 'Deal'\nto start new game"
        msg = 'New Game?'
        return
    while in_play and player_hand.get_value() != 21:
        if dealer_hand.get_value() >= 17:
            in_play = False
            break
        else:
            dealer_hand.add_card(game_deck.deal_card())

    if dealer_hand.busted():
        print('Player wins')
        outcome = "You've Won!"
        msg = 'New Game?'
        score += 1
        in_play = False
    else:
        if dealer_hand.get_value() >= player_hand.get_value():
            print("You've Lost")
            outcome = "You've Lost..."
            score -= 1
            in_play = False
        else:
            print('Player wins')
            outcome = "You've Won!"
            msg = "New Game?"
            score += 1
            in_play = False


def draw(canvas):
    global player_hand, dealer_hand

    if score >= 0:
        score_color = 'Lime'
    else:
        score_color = 'red'

    # Frame Texts
    canvas.draw_text('BlackJack', (WIDTH / 40, HEIGHT / 8), 40, 'black')
    canvas.draw_text('Score: ' + str(score), (WIDTH / 1.5, HEIGHT / 6), 25, score_color)

    # Dealer Hand
    canvas.draw_text('Dealer', (WIDTH / 6, HEIGHT / 3), 25, 'aqua')
    dealer_hand.draw(canvas, [0, HEIGHT / 3])
    dealer_hand.hold(canvas, [0, HEIGHT / 3])
    canvas.draw_text(outcome, (WIDTH / 2, HEIGHT / 3), 20, 'black')

    # Player Hand
    canvas.draw_text('Player', (WIDTH / 6, HEIGHT / 1.5), 25, 'aqua')
    player_hand.draw(canvas, [0, HEIGHT / 1.5])

    canvas.draw_text(msg, (WIDTH / 2, HEIGHT / 1.5), 20, 'black')


frame = simplegui.create_frame("Not Jack Black but Black Jack!", HEIGHT, WIDTH)
frame.set_canvas_background("Green")

frame.add_button("Deal", deal, WIDTH / 3)
frame.add_button("Hit", hit, WIDTH / 3)
frame.add_button("Stand", stand, WIDTH / 3)
frame.set_draw_handler(draw)

deal()
frame.start()
