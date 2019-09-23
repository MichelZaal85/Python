# Guess the number.py
# By Michel Zaal
import simpleguitk as simplegui, random

game_range = 100
counter = 0
def new_game(game_range):
    global secret_number, counter
    secret_number = random.randrange(0, game_range)
    if game_range == 100: 
        counter = 7
    elif game_range == 500: 
        counter = 9
    else:
        counter = 10

    print("""
    ----------------------------
    Welcome to Guess the number!
    ----------------------------
      *cost per game: 1 coin*
    """)
    print(' Game range is set at: [0,%i)' %(game_range))
    print(' You have %i coins left.\n Good Luck!\n' %(counter))

def range100():
    global secret_number, counter, game_range
    secret_number = random.randrange(0,100)
    game_range = 100
    print('\n')
    new_game(game_range)

def range500():
    global secret_number, counter, game_range
    secret_number = random.randrange(0,500)
    game_range = 500
    print('\n')
    new_game(game_range)

def range1000():
    global secret_number, counter, game_range
    number = random.randrange(0,1000)
    game_range = 1000
    print('\n')
    new_game(game_range)

def input_guess(guess):
    guess = int(guess)
    global counter
    counter -= 1
    if guess == secret_number:
        print("""
 You've made me so proud!
    Here have a medal
         _______________
        |####|     |####|
        |####|     |####|
         \###|     |###/
          `##|_____|##'
               (O)
            .-'''''-.
          .'  * * *  `.
         :  *       *  :
        : ~  Gues the ~ :           Joan G Stark 
        : ~   Number  ~ : **http://ascii.co.uk/art/medal**
         :  *       *  :
          `.  * * *  .'
            `-.....-'
        
        """)
        return new_game(game_range)
    
    print('Your guess was: %i' %(guess))
    if counter == 0:
        print('\nOhNo.. No more guesses left.\nThe number you were after was: %i\n\nStarting new game in 3..2..1 GO!\n\n' %(secret_number))
        return new_game(game_range)
    elif guess < secret_number:
        print('Try a higher number')
    else:
        print('Try a lower number')
    print('You have %i coins left.\n' %(counter))

frame = simplegui.create_frame('game', 300, 200, 250)

frame.add_button('Range  [0,100)', range100, 200)
frame.add_button('Range  [0,500)', range500, 200)
frame.add_button('Range [0,1000)', range1000, 200)
frame.add_input('Input guess',input_guess, 50)

frame.start()

new_game(game_range)