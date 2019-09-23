# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math


# helper function to start and restart the game
num_range = 100
count =7
secret_number = 0

print('New game. Range is from 0 to 100')
print('Number of remaining guesses is '+ str(count))
print(' ')

def new_game():
    # initialize global variables used in your code here
    global num_range, count, secret_number

        
    secret_number = random.randrange(0, num_range)
    



# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global num_range, count
    count = 7
    num_range = 100
    print('New game. Range is from 0 to 100')
    print('Number of remaining guesses is '+ str(count))
    print(' ')
    new_game()


def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global num_range, count
    num_range=1000
    count = 10
    print('New game. Range is from 0 to 1000')
    print('Number of remaining guesses is '+ str(count))
    print(' ')
    new_game()
    
    
def input_guess(guess):
    # main game logic goes here	
    global count, num_range, secret_number 
    print('Guess was '+ guess)
    
    
    if secret_number > int(guess): 
        count -= 1
        print('Number of remaining guesses is '+str(count))
        if count ==0: 
            print('You ran out of guesses.  The number was '+ str(secret_number))
            print(' ')
            if num_range == 100: 
                range100()

            elif num_range == 1000: 
                range1000()
            return 
                   
        else: 
            
            print('Higher!')
            print(' ')       
    
        
    elif secret_number < int(guess):
        count -= 1
        print('Number of remaining guesses is '+str(count))
        if count ==0: 
            print('You ran out of guesses.  The number was '+ str(secret_number))
            print(' ')
            if num_range == 100: 
                range100()

            elif num_range == 1000: 
                range1000()
            return 
                   
        else: 
            
            print('Lower!')
            print(' ')
            
    elif secret_number == int(guess): 
        count -= 1
        print('Number of remaining guesses is '+ str(count))
        print('Correct!')
        print(' ')
        if num_range == 100: 
            range100()

        elif num_range == 1000: 
            range1000()
        
    else: 
        print('Please enter an integer!')
    


    
# create frame
f = simplegui.create_frame('Guess the number',200,200) 

# register event handlers for control elements and start frame
f.add_button('Range is [0, 100)', range100, 200)
f.add_button('Range is [0, 1000)', range1000, 200)
f.add_input('Enter a guess', input_guess, 200)

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric




# 
# 
# 









# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

num_range = 100
secret_num = 0
guesses_left = 0

# helper function to start and restart the game
def new_game():
    
    global secret_num, guesses_left
    
    if num_range == 100: 
        guesses_left = 7
        
    elif num_range == 1000: 
        guesses_left = 10
        
    secret_num = random.randrange(0, num_range)
    
    print "New game. Range is [0,", num_range, ")"
    print "Number of remaining guesses is", guesses_left 

# define event handlers for control panel
def range100():
    global num_range
    num_range = 100   
    new_game()

def range1000():
    global num_range 
    num_range = 1000
    new_game()
    
def input_guess(guess):
    global guesses_left
    guess_num =  int(guess)
    guesses_left = guesses_left - 1
    print "Guess was", guess_num
    print "Number of remaining guesses is", guesses_left
    if guess_num == secret_num:
        print "Correct!"
        new_game()
        return
    
    if guesses_left == 0:
        print "You ran out of guesses. Game is over. The number was", secret_num
        new_game()
        return
        
    if guess_num > secret_num:
        print "Lower!"    
    else: 
        print "Higher!"
    
# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements and start frame

frame.add_button("Range is [0, 100)", range100, 200) 
frame.add_button("Range is [0, 1000)", range1000, 200) 
frame.add_input("Enter a guess", input_guess, 200)
            
# call new_game 
new_game()
frame.start()


